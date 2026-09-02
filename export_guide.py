from pathlib import Path
import argparse
import json
import re
import base64
import subprocess
from datetime import datetime
from html import escape

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'docs'
EXPORTS = ROOT / 'exports'

# ---- Folder selection ------------------------------------------------------
# Single source of truth for both selection and compile order is
# src/data/nav_order.json: its top-level key order mirrors build_site.py's NAV
# list (the site's navigation/pagination order).

NAV_ORDER_FILE = ROOT / 'src' / 'data' / 'nav_order.json'
with open(NAV_ORDER_FILE, encoding='utf-8') as fh:
    NAV_ORDER = json.load(fh)          # {rel_path: [slug, rel_path]} in site order

def _folder_of(rel):
    return str(Path(rel).parent)

# Ordered exportable folders: 'user-guide', 'superuser/training', ... (root
# 'index.md' excluded). Order = first appearance in nav_order.json.
FOLDERS = list(dict.fromkeys(_folder_of(rel) for rel in NAV_ORDER if '/' in rel))

def _flag(folder):
    return '--' + folder.split('/')[-1]

def _dest(folder):
    return _flag(folder)[2:].replace('-', '_')

parser = argparse.ArgumentParser(
    description='Export one documentation folder into a single printable HTML '
                'file (order follows src/data/nav_order.json).'
)
for folder in FOLDERS:
    parser.add_argument(_flag(folder), action='store_true',
                        help=f'export {folder}/')
parser.add_argument('--out', default=None,
                    help='output file name (default: exports/<folder>.html)')
args = parser.parse_args()

# No flag given -> user-guide (backwards-compatible default).
chosen = 'user-guide'
for folder in FOLDERS:
    if getattr(args, _dest(folder)):
        chosen = folder
        break

# Pages of the chosen folder, already in nav_order.json order.
PAGES = [rel for rel in NAV_ORDER if _folder_of(rel) == chosen]
missing = [rel for rel in PAGES if not (DOCS / rel).exists()]
if missing:
    print('WARNING: skipping pages not found on disk:', *missing, sep='\n  ')
PAGES = [rel for rel in PAGES if (DOCS / rel).exists()]
if not PAGES:
    parser.error(f'no pages found in nav_order.json under {chosen}/')

GROUP_LABEL = ('User Guide' if chosen == 'user-guide'
               else chosen.rsplit('/', 1)[-1].replace('-', ' ').title())
doc_title = f'ORION NanoFab {GROUP_LABEL}'
OUT = EXPORTS / (args.out or (chosen.rsplit('/', 1)[-1] + '.html'))


def get_latest_git_author():
    """Return the author of the latest commit affecting User Guide files."""
    try:
        paths = [str((DOCS / rel).relative_to(ROOT)) for rel in PAGES]

        result = subprocess.run(
            [
                'git',
                '-C', str(ROOT),
                'log',
                '-1',
                '--format=%an',
                '--',
                *paths,
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        return result.stdout.strip() or 'Unknown'

    except (subprocess.CalledProcessError, FileNotFoundError):
        return 'Unknown'


def document_information_html():
    generated = datetime.now().astimezone().strftime(
        '%Y-%m-%d %H:%M %z'
    )

    # Convert +0800 -> +08:00
    if len(generated) >= 5:
        generated = generated[:-2] + ':' + generated[-2:]

    author = get_latest_git_author()

    return f'''
    <section class="document-information">
        <h2>Document information</h2>

        <div class="doc-info-row">
            <div class="doc-info-label">Generated</div>
            <div>{escape(generated)}</div>
        </div>

        <div class="doc-info-row">
            <div class="doc-info-label">Git author</div>
            <div>{escape(author)}</div>
        </div>
    </section>
    '''

def strip_frontmatter(text):
    """Remove YAML frontmatter from Markdown."""
    return text.split('---\n', 2)[2] if text.startswith('---\n') else text

def inline(s):
    """Convert inline Markdown to HTML."""
    s = escape(s.strip())
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*(.+?)\*(?!\*)', r'<em>\1</em>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    return s

def image_to_base64(img_path):
    """Convert image file to base64 for embedding."""
    if not img_path.exists():
        return None
    with open(img_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def parse_markdown_to_html(md_path):
    """Parse Markdown file and return HTML string."""
    text = strip_frontmatter(md_path.read_text(encoding='utf-8'))
    lines = text.splitlines()
    html_parts = []
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()
        st = line.strip()

        # Handle images
        m = re.match(r'^!\[(.*?)\]\((.*?)\)$', st)
        if m:
            img_rel = m.group(2)
            img_path = (md_path.parent / img_rel).resolve()
            caption = None
            if i + 1 < len(lines) and re.match(r'^\*.+\*$', lines[i + 1].strip()):
                caption = lines[i + 1].strip().strip('*')
                i += 1

            if img_path.exists():
                b64 = image_to_base64(img_path)
                html_parts.append(f'<figure><img src="data:image/png;base64,{b64}" alt="figure">')
                if caption:
                    html_parts.append(f'<figcaption>{escape(caption)}</figcaption>')
                html_parts.append('</figure>')
            i += 1
            continue

        # Handle headings
        if st.startswith('# '):
            html_parts.append(f'<h1>{inline(st[2:])}</h1>')
            i += 1
            continue
        if st.startswith('## '):
            html_parts.append(f'<h2>{inline(st[3:])}</h2>')
            i += 1
            continue
        if st.startswith('### '):
            html_parts.append(f'<h3>{inline(st[4:])}</h3>')
            i += 1
            continue

        # Handle blockquotes (warnings)
        if st.startswith('> '):
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                quote_lines.append(lines[i].strip().lstrip('>').strip())
                i += 1
            html_parts.append(f'<blockquote class="warning">{inline(" ".join(quote_lines))}</blockquote>')
            continue

        # Handle ordered lists
        if re.match(r'^\d+\.\s+', st):
            html_parts.append('<ol>')
            while i < len(lines) and re.match(r'^\d+\.\s+', lines[i].strip()):
                item_text = re.sub(r'^\d+\.\s+', '', lines[i].strip())
                html_parts.append(f'<li>{inline(item_text)}</li>')
                i += 1
            html_parts.append('</ol>')
            continue

        # Handle unordered lists
        if st.startswith('- '):
            html_parts.append('<ul>')
            while i < len(lines) and lines[i].strip().startswith('- '):
                item_text = lines[i].strip()[2:]
                html_parts.append(f'<li>{inline(item_text)}</li>')
                i += 1
            html_parts.append('</ul>')
            continue

        # Handle paragraphs
        if st:
            paras = [st]
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r'^(#|>|\d+\.\s+|-\s+|!\[)', lines[i].strip()):
                paras.append(lines[i].strip())
                i += 1
            html_parts.append(f'<p>{inline(" ".join(paras))}</p>')
            continue

        i += 1

    return '\n'.join(html_parts)

# Generate HTML document
OUT.parent.mkdir(exist_ok=True)

html_content = []
for n, rel in enumerate(PAGES):
    page_html = parse_markdown_to_html(DOCS / rel)
    html_content.append(page_html)
    if n < len(PAGES) - 1:
        html_content.append('<div class="page-break"></div>')

# Build complete HTML document
full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{doc_title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            color: #333;
        }}
        h1 {{ font-size: 28px; margin-top: 40px; margin-bottom: 16px; page-break-after: avoid; }}
        h2 {{ font-size: 22px; margin-top: 32px; margin-bottom: 12px; page-break-after: avoid; }}
        h3 {{ font-size: 18px; margin-top: 24px; margin-bottom: 8px; page-break-after: avoid; }}
        p {{ margin: 12px 0; }}
        ul, ol {{ margin: 12px 0; padding-left: 24px; }}
        li {{ margin: 6px 0; }}
        code {{ background: #f5f5f5; padding: 2px 6px; font-family: 'Courier New', monospace; }}
        blockquote.warning {{
            background: #fff6df;
            border-left: 4px solid #d18b00;
            padding: 12px 16px;
            margin: 16px 0;
            page-break-inside: avoid;
        }}
        figure {{
            max-width: 100%;
            text-align: center;
            margin: 20px 0;
            page-break-inside: avoid;
        }}
        figure img {{
            max-width: 100%;
            height: auto;
        }}
        figcaption {{
            font-size: 12px;
            color: #666;
            margin-top: 8px;
            font-style: italic;
        }}
        .page-break {{
            page-break-after: always;
        }}

        .document-information {{
            margin-top: 64px;
            padding: 24px 0 32px;
            border-top: 1px solid #d9dde5;
            border-bottom: 1px solid #d9dde5;
            page-break-inside: avoid;
            }}

        .document-information h2 {{
            font-size: 20px;
            margin: 0 0 24px;
        }}

        .doc-info-row {{
            display: grid;
            grid-template-columns: 180px 1fr;
            margin: 10px 0;
            font-size: 17px;
        }}

        .doc-info-label {{
            color: #6b7280;
        }}
        /* Print styles */
        @media print {{
            body {{ padding: 0; }}
            h1, h2, h3 {{ page-break-after: avoid; }}
            figure {{ page-break-inside: avoid; }}
            blockquote {{ page-break-inside: avoid; }}
            ul, ol {{ page-break-inside: avoid; }}
        }}
    </style>
</head>

<body>
    <h1>{doc_title}</h1>
    <p><em>Generated from the maintained Markdown documentation ({chosen}/).</em></p>
    <blockquote class="warning">
        <strong>Important:</strong> This is an exported copy. The authoritative source is the online/Markdown documentation.
        Future updates may not be reflected here.
    </blockquote>
    <hr>
    {chr(10).join(html_content)}

{document_information_html()}

</body>
</html>
"""

OUT.write_text(full_html, encoding='utf-8')
print(f'{GROUP_LABEL} exported to: {OUT}')
print('Open in browser and press Cmd+P to print/save as PDF.')
