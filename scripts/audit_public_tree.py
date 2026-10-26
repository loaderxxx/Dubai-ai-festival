#!/usr/bin/env python3
"""Audit the public repository boundary, local links and self-contained SVG assets.

This is a preventive local check, not an independent source-quality or privacy guarantee.
"""
from __future__ import annotations
import json,re,sys,hashlib
from pathlib import Path
from urllib.parse import unquote,urlsplit
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
APPROVED_BINARY={'assets/russian-ai-intelligence-banner.png':'5166d8abcf6161892229d2276b5ab1d317e179162c18e5820f410782a549ca8d'}
errors=[];warnings=[];checked_links=0;checked_anchors=0;svg_count=0
def heading_anchors(path):
    body=re.sub(r"```.*?```","",path.read_text(),flags=re.S)
    counts={};anchors=set()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$",body,flags=re.M):
        heading=re.sub(r"!?\[([^]]+)\]\([^)]+\)",r"\1",heading)
        heading=re.sub(r"<[^>]+>","",heading).strip().casefold()
        anchor=re.sub(r"[^\w\- ]","",heading).replace(" ","-")
        n=counts.get(anchor,0);counts[anchor]=n+1
        anchors.add(anchor if n==0 else f"{anchor}-{n}")
    return anchors

# Public research may link public company sites; never import the authenticated directory.
blocked_fragments=['app.'+'dubaiaifestival.com','attendees-'+'directory','full-research-'+'snapshot-2026-10-26.zip','dubai-festival-private-'+'publication']
credential=re.compile(r'''(?i)(?:access_token|refresh_token|client_secret|authorization)["']?\s*[:=]\s*["'](?:Bearer\s+)?[A-Za-z0-9_.~+/=-]{16,}["']''')
email=re.compile(r'(?<![\w@])[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}(?![\w@])')
files=[p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts]
for p in files:
    relative=p.relative_to(ROOT).as_posix()
    if p.suffix.lower() in {'.png','.jpg','.jpeg','.webp','.gif','.pdf','.zip'}:
        if relative not in APPROVED_BINARY or hashlib.sha256(p.read_bytes()).hexdigest()!=APPROVED_BINARY[relative]:
            errors.append(f'Unexpected or modified binary artifact needs explicit provenance review: {relative}')
        continue
    try:text=p.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        errors.append(f'Non-UTF-8 artifact: {relative}');continue
    for marker in blocked_fragments:
        if marker in text.casefold() or marker in relative.casefold(): errors.append(f'Private-source marker in {relative}: {marker}')
    if credential.search(text): errors.append(f'Possible credential value in {relative}')
    if p.suffix.lower()!='.py' and email.search(text): warnings.append(f'Email-like text requires human review: {relative}')
    if p.suffix.lower()=='.json':
        try:json.loads(text)
        except json.JSONDecodeError as exc:errors.append(f'Invalid JSON {relative}: {exc}')
    if p.suffix.lower()=='.svg':
        svg_count+=1
        try:tree=ET.fromstring(text)
        except ET.ParseError as exc:errors.append(f'Invalid SVG {relative}: {exc}');continue
        for node in tree.iter():
            tag=node.tag.split('}')[-1].casefold()
            if tag in {'script','foreignobject','iframe','audio','video','image'}:errors.append(f'Active/embedded SVG element {tag} in {relative}')
            for key,value in node.attrib.items():
                key=key.split('}')[-1].casefold()
                if key.startswith('on'):errors.append(f'SVG event handler in {relative}')
                if key in {'href','src'} and not value.startswith('#'):errors.append(f'Non-local SVG reference in {relative}')
        if not any(n.tag.split('}')[-1]=='title' for n in tree.iter()):warnings.append(f'SVG missing accessible title: {relative}')
    if p.suffix.lower()=='.md':
        clean=re.sub(r'```.*?```','',text,flags=re.S)
        for link in re.findall(r'\]\(([^)]+)\)',clean):
            url=link.split(' "',1)[0].strip('<>')
            parsed=urlsplit(url)
            if parsed.scheme or parsed.netloc:continue
            if not parsed.path and not parsed.fragment:continue
            checked_links+=1
            target=(p.parent/unquote(parsed.path)).resolve() if parsed.path else p
            if not target.is_relative_to(ROOT):errors.append(f'Local link escapes public tree: {relative} -> {url}')
            elif not target.exists():errors.append(f'Broken local link: {relative} -> {url}')
            elif parsed.fragment and target.suffix.lower()=='.md':
                checked_anchors+=1
                if unquote(parsed.fragment) not in heading_anchors(target):errors.append(f'Unresolved Markdown heading anchor: {relative} -> {url}')
report={'result':'PASS' if not errors else 'FAIL','scope':'Local public-source boundary markers, credential patterns, UTF-8/JSON, local Markdown paths and passive self-contained SVGs; not source completeness or independent privacy certification.','files_checked':len(files),'local_links_checked':checked_links,'heading_anchors_checked':checked_anchors,'svg_assets_checked':svg_count,'errors':errors,'warnings':warnings}
print(json.dumps(report,ensure_ascii=False,indent=2))
if errors:sys.exit(1)
