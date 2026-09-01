from pathlib import Path
import re, html, json, subprocess, argparse, time

ROOT=Path(__file__).resolve().parent; DOCS=ROOT/'docs'
parser=argparse.ArgumentParser(description='Build ORION NanoFab documentation from Markdown.')
group=parser.add_mutually_exclusive_group()
group.add_argument('--exclude-drafts', action='store_true', help='Exclude pages whose frontmatter status is draft.')
group.add_argument('--drafts-only', action='store_true', help='Build only pages whose frontmatter status is draft.')
args=parser.parse_args()

def git_signature(path):
    """Return last Git editor metadata for a documentation file. No shell is used."""
    try:
        rel=str(path.relative_to(ROOT))
        r=subprocess.run(['git','log','-1','--format=%an%x1f%ae%x1f%aI%x1f%h','--',rel],cwd=ROOT,capture_output=True,text=True,timeout=5,check=False)
        if r.returncode==0 and r.stdout.strip():
            name,email,date,commit=r.stdout.strip().split('\x1f',3)
            return {'editor':name,'email':email,'edited':date,'commit':commit}
    except (OSError,ValueError,subprocess.SubprocessError):
        pass
    return {}

def get_all_contributors():
    """Return list of all unique contributors (name, email) from Git."""
    try:
        r=subprocess.run(['git','log','--format=%an%x1f%ae','--','docs/'],cwd=ROOT,capture_output=True,text=True,timeout=10,check=False)
        if r.returncode==0 and r.stdout.strip():
            seen=set()
            contributors=[]
            for line in r.stdout.strip().split('\n'):
                if line and '\x1f' in line:
                    name,email=line.split('\x1f',1)
                    key=(name.strip(),email.strip())
                    if key not in seen:
                        seen.add(key)
                        contributors.append(key)
            return contributors
    except (OSError,subprocess.SubprocessError):
        pass
    return []

NAV=[('home','index.md'),('before','user-guide/before-you-start.md'),('loading','user-guide/loading-unloading.md'),('start','user-guide/starting-session.md'),('trimercheck','user-guide/trimer-check.md'),('imaging','user-guide/imaging.md'),('patterning','user-guide/patterning.md'),('neon','user-guide/neon.md'),('end','user-guide/ending-session.md'),('warning','user-guide/warning-signals.md'),('training','superuser/training/index.md'),('safetytraining','superuser/training/safety-training.md'),('session1','superuser/training/session-1.md'),('session2','superuser/training/session-2.md'),('competency','superuser/training/competency-test.md'),('maintenance','superuser/maintenance/index.md'),('routine','superuser/maintenance/routine-checks.md'),('trimer','superuser/maintenance/trimer-formation.md'),('ln2','superuser/maintenance/ln2-system.md'),('gas','superuser/maintenance/gas-cylinders.md'),('source','superuser/maintenance/source-maintenance.md'),('shutdown','superuser/error-recovery/shutdown/planned-shutdown.md'),('powerup','superuser/error-recovery/shutdown/power-up.md'),('vacuumrecovery','superuser/error-recovery/shutdown/vacuum-recovery.md'),('gfisrecovery','superuser/error-recovery/shutdown/gfis-recovery.md'),('trouble','superuser/error-recovery/troubleshooting/index.md'),('chamber','superuser/error-recovery/troubleshooting/main-chamber-vent.md'),('overheat','superuser/error-recovery/troubleshooting/gun-overheat.md'),('vacuum','superuser/error-recovery/troubleshooting/vacuum-problems.md'),('comm','superuser/error-recovery/troubleshooting/communication-firmware.md'),('trimerproblem','superuser/error-recovery/troubleshooting/trimer-problems.md'),('imageproblem','superuser/error-recovery/troubleshooting/image-problems.md'),('safety','safety/index.md'),('o2','safety/oxygen-nitrogen.md'),('fire','safety/fire-suppression.md'),('hv','safety/high-voltage.md'),('chambersafety','safety/vacuum-chamber.md'),('emergency','safety/emergency.md'),('system','reference/system-overview.md'),('gfis','reference/gfis-controls.md'),('vacref','reference/vacuum-system.md'),('concepts','reference/imaging-concepts.md'),('glossary','reference/glossary.md'),('originals','reference/original-documents.md'),('infobase','information-base/index.md')]
for p in sorted((DOCS/'information-base').glob('*.md')):
    if p.name!='index.md': NAV.append(('src-'+p.stem, str(p.relative_to(DOCS))))
def inline_md(text):
    text=html.escape(text, quote=False)
    text=re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', text)
    text=re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text=re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text=re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)
    return text

def markdown_to_html(text):
    """Small dependency-free Markdown renderer for this documentation set."""
    out=[]; para=[]; in_code=False; code=[]; list_type=None
    def flush_para():
        nonlocal para
        if para:
            out.append('<p>'+inline_md(' '.join(x.strip() for x in para))+'</p>'); para=[]
    def close_list():
        nonlocal list_type
        if list_type: out.append(f'</{list_type}>'); list_type=None
    for raw in text.splitlines():
        line=raw.rstrip()
        if line.startswith('```'):
            flush_para(); close_list()
            if in_code: out.append('<pre><code>'+html.escape('\n'.join(code))+'</code></pre>'); code=[]; in_code=False
            else: in_code=True
            continue
        if in_code: code.append(line); continue
        if not line.strip(): flush_para(); close_list(); continue
        m=re.match(r'^(#{1,6})\s+(.*)$',line)
        if m:
            flush_para(); close_list(); n=len(m.group(1)); out.append(f'<h{n}>'+inline_md(m.group(2))+f'</h{n}>'); continue
        m=re.match(r'^\s*[-*]\s+(.*)$',line)
        if m:
            flush_para()
            if list_type!='ul': close_list(); out.append('<ul>'); list_type='ul'
            out.append('<li>'+inline_md(m.group(1))+'</li>'); continue
        m=re.match(r'^\s*\d+[.)]\s+(.*)$',line)
        if m:
            flush_para()
            if list_type!='ol': close_list(); out.append('<ol>'); list_type='ol'
            out.append('<li>'+inline_md(m.group(1))+'</li>'); continue
        if line.startswith('>'):
            flush_para(); close_list(); out.append('<blockquote>'+inline_md(line.lstrip('> ').strip())+'</blockquote>'); continue
        if re.match(r'^\s*\|.*\|\s*$',line):
            flush_para(); close_list(); out.append('<p class="md-table-line">'+inline_md(line)+'</p>'); continue
        para.append(line)
    flush_para(); close_list()
    if in_code: out.append('<pre><code>'+html.escape('\n'.join(code))+'</code></pre>')
    return '\n'.join(out)
def frontmatter_status(path):
    text=path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        return ''
    try:
        _,fm,_=text.split('---\n',2)
    except ValueError:
        return ''
    for line in fm.splitlines():
        if line.lower().startswith('status:'):
            return line.split(':',1)[1].strip().strip('\"').lower()
    return ''

def include_page(path):
    status=frontmatter_status(path)
    if args.exclude_drafts:
        return status != 'draft'
    if args.drafts_only:
        return status == 'draft'
    return True

def parse(path):
    text=path.read_text(encoding='utf-8'); meta={}
    if text.startswith('---\n'):
        _,fm,text=text.split('---\n',2); key=None
        for line in fm.splitlines():
            if line.startswith('  - ') and key=='sources': meta.setdefault('sources',[]).append(line[4:].strip().strip('"'))
            elif ':' in line:
                k,v=line.split(':',1); key=k.strip(); val=v.strip().strip('"'); meta[key]=([] if key=='sources' and not val else val)
    body=markdown_to_html(text)
    # SPA is served from project root, while image paths in MD are relative to docs subfolders.
    body=body.replace('src="../assets/','src="assets/').replace('src="../../assets/','src="assets/').replace('src="../../../assets/','src="assets/').replace('src="../../../../assets/','src="assets/')
    # source-file links from docs are also rooted at project root in the generated SPA.
    body=body.replace('href="../../sources/','href="sources/').replace('href="../../../sources/','href="sources/')
    badge='<span class="badge super">SUPERUSER ONLY</span>' if meta.get('access')=='superuser' else '<span class="badge">ALL USERS</span>'
    sig=git_signature(path)
    info=[]
    if meta.get('revision'): info.append(('Revision',meta['revision']))
    if meta.get('status'): info.append(('Status',meta['status']))
    if meta.get('owner'): info.append(('Owner',meta['owner']))
    if meta.get('last-reviewed'): info.append(('Last reviewed',meta['last-reviewed']))
    if sig:
        info.extend([('Last edited by',sig['editor']),('Last modified',sig['edited']),('Git revision',sig['commit'])])
    elif meta.get('edited-by'):
        info.extend([('Last edited by',meta.get('edited-by','')),('Last modified',meta.get('edited-date','not recorded'))])
    if info:
        body += '<details class="doc-info"><summary>Document information</summary><dl>'+''.join('<dt>'+html.escape(str(k))+'</dt><dd>'+html.escape(str(v))+'</dd>' for k,v in info)+'</dl></details>'
    sources=meta.get('sources',[])
  
    if sources: body += '<p class="source"><b>Sources:</b> '+', '.join(html.escape(x) for x in sources)+'</p>'

    # Inject pagination links from frontmatter
    nav_prev_key = meta.get('nav_previous')
    nav_prev_path = meta.get('nav_previous_path')
    nav_next_key = meta.get('nav_next')
    nav_next_path = meta.get('nav_next_path')
    
    if nav_prev_path or nav_next_path:
        body += '<nav class="pagination">'
        if nav_prev_path:
            # Extract the page key from NAV mapping: 'user-guide/loading-unloading.md' → find its key
            prev_page_key = next((k for k, rel in NAV if rel == nav_prev_path.lstrip('./')), None)
            if prev_page_key:
                body += f'<a href="#" data-page="{prev_page_key}" class="pagination-prev">← {nav_prev_key or "Previous"}</a>'
        if nav_next_path:
            # Extract the page key from NAV mapping: 'user-guide/loading-unloading.md' → find its key
            next_page_key = next((k for k, rel in NAV if rel == nav_next_path.lstrip('./')), None)
            if next_page_key:
                body += f'<a href="#" data-page="{next_page_key}" class="pagination-next">{nav_next_key or "Next"} →</a>'
        body += '</nav>'
    
    result='<div class="crumb">ORION NanoFab Documentation</div>'+badge+body


    # Add contributors list to home page only
    if path.name=='index.md':
        contributors=get_all_contributors()
        if contributors:
            result+='<hr style="margin:40px 0;border:none;border-top:1px solid #e5e7eb"><div class="contributors"><h3>Documentation Contributors</h3><ul style="list-style:none;padding:0;font-size:12px">'
            for name,email in contributors:
                result+=f'<li style="padding:3px 0"><strong>{html.escape(name)}</strong> &lt;{html.escape(email)}&gt;</li>'
            result+='</ul></div>'
    return result


pages={}
for key,rel in NAV:
    p=DOCS/rel
    if p.exists() and include_page(p): pages[key]=parse(p)

def app_js_source():
    js_path = ROOT/'assets/app.js'
    if js_path.exists() and js_path.stat().st_size > 0:
        return js_path.read_text(encoding='utf-8')

    try:
        r = subprocess.run(['git','show','HEAD:assets/app.js'], cwd=ROOT, capture_output=True, text=True, check=False)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout
    except (OSError, ValueError):
        pass

    return """function setRole(role){localStorage.setItem('orionRole',role);document.body.classList.toggle('superuser',role==='superuser');document.querySelectorAll('[data-role]').forEach(b=>b.classList.toggle('active',b.dataset.role===role));document.querySelectorAll('.super-link').forEach(a=>a.style.opacity=role==='superuser'?'1':'.48');}
const pages={};
function render(p){if(!pages[p])p='home';if(document.querySelector(`[data-page="${p}"].super-link`)&&!document.body.classList.contains('superuser'))p='access';document.getElementById('content').innerHTML=p==='access'?'<h1>Superuser access required</h1><p>Switch the prototype role to Superuser to preview this section. Production access must be enforced by authentication.</p>':pages[p];document.querySelectorAll('.nav a').forEach(a=>a.classList.toggle('active',a.dataset.page===p));if(p!=='access')expandForPage(p);window.scrollTo(0,0)}
function pageTitle(htmlText){const m=htmlText.match(/<h1[^>]*>(.*?)<\/h1>/i);return m?stripHtml(m[1]):'Documentation'}
function stripHtml(v){const d=document.createElement('div');d.innerHTML=v;return (d.textContent||'').replace(/\s+/g,' ').trim()}
const searchIndex=Object.entries(pages).map(([key,value])=>({key,title:pageTitle(value),text:stripHtml(value)}));
function expandForPage(p){document.querySelectorAll('.nav-group,.nav-subgroup').forEach(d=>d.open=false);const link=document.querySelector(`[data-page="${CSS.escape(p)}"]`);if(!link)return;let el=link.parentElement;while(el){if(el.tagName==='DETAILS')el.open=true;el=el.parentElement}}
"""

js = app_js_source()
pattern = r'const pages=\{.*?\};\s*function render'
# Rebuild app.js from scratch with fresh pages object
js_base = r"""function setRole(role){localStorage.setItem('orionRole',role);document.body.classList.toggle('superuser',role==='superuser');document.querySelectorAll('[data-role]').forEach(b=>b.classList.toggle('active',b.dataset.role===role));document.querySelectorAll('.super-link').forEach(a=>a.style.opacity=role==='superuser'?'1':'.48');}
function render(p){if(!pages[p])p='home';if(document.querySelector(`[data-page="${p}"].super-link`)&&!document.body.classList.contains('superuser'))p='access';document.getElementById('content').innerHTML=p==='access'?'<h1>Superuser access required</h1><p>Switch the prototype role to Superuser to preview this section. Production access must be enforced by authentication.</p>':pages[p];document.querySelectorAll('.nav a').forEach(a=>a.classList.toggle('active',a.dataset.page===p));if(p!=='access')expandForPage(p);window.scrollTo(0,0)}
function pageTitle(htmlText){const m=htmlText.match(/<h1[^>]*>(.*?)<\/h1>/i);return m?stripHtml(m[1]):'Documentation'}
function stripHtml(v){const d=document.createElement('div');d.innerHTML=v;return (d.textContent||'').replace(/\s+/g,' ').trim()}
const searchIndex=Object.entries(pages).map(([key,value])=>({key,title:pageTitle(value),text:stripHtml(value)}));
function expandForPage(p){document.querySelectorAll('.nav-group,.nav-subgroup').forEach(d=>d.open=false);const link=document.querySelector(`[data-page="${CSS.escape(p)}"]`);if(!link)return;let el=link.parentElement;while(el){if(el.tagName==='DETAILS')el.open=true;el=el.parentElement}}
function performSearch(query){const q=query.toLowerCase();const results=searchIndex.filter(e=>e.title.toLowerCase().includes(q)||e.text.toLowerCase().includes(q)).slice(0,10);const resultsDiv=document.getElementById('search-results');if(!q){resultsDiv.hidden=true;return;}resultsDiv.hidden=false;resultsDiv.innerHTML='';if(results.length===0){resultsDiv.innerHTML='<div class="search-empty">No results found</div>';return;}results.forEach(r=>{const div=document.createElement('div');div.className='search-result';const title=document.createElement('div');title.className='search-title';title.textContent=r.title;const snippet=document.createElement('div');snippet.className='search-snippet';snippet.textContent=r.text.substring(0,80)+'...';div.appendChild(title);div.appendChild(snippet);div.onclick=e=>{e.preventDefault();render(r.key);document.getElementById('doc-search').value='';resultsDiv.hidden=true;};div.style.cursor='pointer';resultsDiv.appendChild(div);});}
document.addEventListener('DOMContentLoaded',function(){const saved=localStorage.getItem('orionRole')||'user';setRole(saved);document.querySelectorAll('[data-page]').forEach(a=>a.addEventListener('click',function(e){e.preventDefault();render(this.dataset.page)}));document.getElementById('doc-search').addEventListener('input',e=>performSearch(e.target.value));render('home');});
"""

# Inject fresh pages object at the top of the JS file
js = 'const pages=' + json.dumps(pages, ensure_ascii=False) + ';\n' + js_base
# Inject fresh pages object at the top of the JS file
js = 'const pages=' + json.dumps(pages, ensure_ascii=False) + ';\n' + js_base
(ROOT/'assets').mkdir(exist_ok=True)
(ROOT/'assets/app.js').write_text(js, encoding='utf-8')
# Cache-bust the generated JavaScript reference so browsers do not keep an older embedded page bundle.
index_path=ROOT/'index.html'
index=index_path.read_text(encoding='utf-8')
stamp=str(int(time.time()))
index=re.sub(r'assets/app\.js(?:\?v=[0-9]+)?', 'assets/app.js?v='+stamp, index)
index_path.write_text(index,encoding='utf-8')
mode='all pages' if not (args.exclude_drafts or args.drafts_only) else ('excluding drafts' if args.exclude_drafts else 'drafts only')
print(f'Project root: {ROOT}')
print(f'Markdown source: {DOCS}')
print(f'Generated bundle: {ROOT / "assets/app.js"}')
print(f'Open this file: {index_path}')
print(f'Build mode: {mode}')
print(f'Built {len(pages)} pages from Markdown.')
