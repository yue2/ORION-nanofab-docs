#!/usr/bin/env python3
"""Build the all-user User Guide PDF from local Markdown and local image assets."""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, ListFlowable, ListItem, KeepTogether

ROOT=Path(__file__).resolve().parent; DOCS=ROOT/'docs'; OUT=ROOT/'exports'/'orion-nanofab-user-guide.pdf'
PAGES=['user-guide/before-you-start.md','user-guide/loading-unloading.md','user-guide/starting-session.md','user-guide/trimer-check.md','user-guide/imaging.md','user-guide/patterning.md','user-guide/neon.md','user-guide/ending-session.md','user-guide/warning-signals.md']
styles=getSampleStyleSheet(); styles.add(ParagraphStyle(name='CoverTitle',parent=styles['Title'],fontSize=26,leading=31,alignment=TA_CENTER,spaceAfter=10)); styles.add(ParagraphStyle(name='Warn',parent=styles['BodyText'],backColor='#fff6df',borderColor='#d18b00',borderWidth=1,borderPadding=8,spaceBefore=7,spaceAfter=7)); styles['BodyText'].leading=14

def strip_frontmatter(text):
    return text.split('---\n',2)[2] if text.startswith('---\n') else text

def inline(s):
    s=escape(s.strip())
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s); s=re.sub(r'(?<!\*)\*(.+?)\*(?!\*)',r'<i>\1</i>',s); s=re.sub(r'`(.+?)`',r'<font name="Courier">\1</font>',s)
    return s

def image_path(md_path,raw):
    return (md_path.parent/raw).resolve()

def add_image(story,path,caption=None):
    if not path.exists(): return
    im=Image(str(path)); maxw=165*mm; maxh=190*mm; scale=min(maxw/im.imageWidth,maxh/im.imageHeight,1); im.drawWidth*=scale; im.drawHeight*=scale
    parts=[im]
    if caption: parts += [Spacer(1,2*mm),Paragraph(inline(caption),styles['Caption'])]
    story.append(KeepTogether(parts)); story.append(Spacer(1,4*mm))

def parse_page(md_path):
    text=strip_frontmatter(md_path.read_text(encoding='utf-8')); lines=text.splitlines(); story=[]; i=0
    while i<len(lines):
        line=lines[i].rstrip(); st=line.strip()
        m=re.match(r'^!\[(.*?)\]\((.*?)\)$',st)
        if m:
            cap=None
            if i+1<len(lines) and re.match(r'^\*.+\*$',lines[i+1].strip()): cap=lines[i+1].strip().strip('*'); i+=1
            add_image(story,image_path(md_path,m.group(2)),cap); i+=1; continue
        if st.startswith('# '): story.append(Paragraph(inline(st[2:]),styles['Heading1'])); i+=1; continue
        if st.startswith('## '): story.append(Paragraph(inline(st[3:]),styles['Heading2'])); i+=1; continue
        if st.startswith('### '): story.append(Paragraph(inline(st[4:]),styles['Heading3'])); i+=1; continue
        if st.startswith('> '):
            q=[]
            while i<len(lines) and lines[i].strip().startswith('>'):
                q.append(lines[i].strip().lstrip('>').strip()); i+=1
            story.append(Paragraph(inline(' '.join(q)),styles['Warn'])); continue
        if re.match(r'^\d+\.\s+',st):
            items=[]
            while i<len(lines) and re.match(r'^\d+\.\s+',lines[i].strip()):
                items.append(ListItem(Paragraph(inline(re.sub(r'^\d+\.\s+','',lines[i].strip())),styles['BodyText']))); i+=1
            story.append(ListFlowable(items,bulletType='1',leftIndent=18)); story.append(Spacer(1,2*mm)); continue
        if st.startswith('- '):
            items=[]
            while i<len(lines) and lines[i].strip().startswith('- '):
                items.append(ListItem(Paragraph(inline(lines[i].strip()[2:]),styles['BodyText']))); i+=1
            story.append(ListFlowable(items,bulletType='bullet',leftIndent=18)); story.append(Spacer(1,2*mm)); continue
        if st:
            paras=[st]; i+=1
            while i<len(lines) and lines[i].strip() and not re.match(r'^(#|>|\d+\.\s+|-\s+|!\[)',lines[i].strip()): paras.append(lines[i].strip()); i+=1
            story.append(Paragraph(inline(' '.join(paras)),styles['BodyText'])); story.append(Spacer(1,2*mm)); continue
        i+=1
    return story

OUT.parent.mkdir(exist_ok=True)
doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=17*mm,leftMargin=17*mm,topMargin=16*mm,bottomMargin=18*mm,title='ORION NanoFab User Guide')
story=[]
cover=ROOT/'assets/img/general/orion-nanofab.png'
if cover.exists(): add_image(story,cover)
story += [Paragraph('ORION NanoFab User Guide',styles['CoverTitle']),Paragraph('Generated from the maintained Markdown documentation.',styles['BodyText']),Spacer(1,4*mm),Paragraph('<b>Controlled source:</b> online/Markdown documentation. Exported copies may become outdated.',styles['Warn']),PageBreak()]
for n,rel in enumerate(PAGES):
    story += parse_page(DOCS/rel)
    if n<len(PAGES)-1: story.append(PageBreak())
doc.build(story)
print(OUT)
