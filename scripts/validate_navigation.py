#!/usr/bin/env python3
"""Offline Markdown/SVG checks. No external fetching; no web-truth claim."""
import argparse
import json
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit


def unfence(text):
    """Drop fenced code so sample syntax is not mistaken for navigation."""
    lines, fence = [], None
    for line in text.splitlines():
        m = re.match(r'^\s*(`{3,}|~{3,})', line)
        if m:
            if fence is None:
                fence = m.group(1)[0]
            elif m.group(1)[0] == fence:
                fence = None
            lines.append('')
        else:
            lines.append('' if fence else line)
    return '\n'.join(lines)


def slugify(text):
    # GitHub-style slugs for the ordinary ATX headings used in this repository.
    text = re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'<[^>]*>', '', text).strip().lower()
    text = ''.join(c for c in text if c in '-_ ' or unicodedata.category(c)[0] in 'LN')
    return text.replace(' ', '-')


def headings(path):
    found, seen = set(), {}
    for line in unfence(path.read_text(encoding='utf-8')).splitlines():
        match = re.match(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$', line)
        if not match:
            continue
        slug = slugify(match.group(1))
        n = seen.get(slug, 0)
        seen[slug] = n + 1
        found.add(slug if n == 0 else f'{slug}-{n}')
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    errors = []
    md_files = sorted(root.rglob('*.md'))
    svg_files = sorted(root.rglob('*.svg'))
    links = images = anchors = 0
    heading_cache = {}
    nav_names = {'README.md', 'README.ru.md', 'research-status.md', 'source-policy.md'}
    for md in md_files:
        rel = md.relative_to(root).as_posix()
        body = unfence(md.read_text(encoding='utf-8'))
        if md.name in nav_names and re.search(r'</?[A-Za-z][^>]*>', body):
            errors.append(f'{rel}: raw HTML in navigation; use Markdown or SVG image embeds')
        for match in re.finditer(r'(!?)\[([^\]\n]*)\]\(([^\s)]+)(?:\s+"[^"]*")?\)', body):
            is_image, label, link = match.groups()
            links += 1
            if is_image:
                images += 1
                if not label.strip():
                    errors.append(f'{rel}: image missing descriptive alt text: {link}')
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                if parsed.scheme not in {'https', 'http', 'mailto'}:
                    errors.append(f'{rel}: unexpected link scheme: {link}')
                continue
            path = unquote(parsed.path)
            target = (md.parent / path).resolve() if path else md
            if not target.is_relative_to(root):
                errors.append(f'{rel}: link escapes repository: {link}')
                continue
            if not target.exists():
                errors.append(f'{rel}: missing target: {link}')
                continue
            if parsed.fragment and target.suffix.lower() == '.md':
                anchors += 1
                if target not in heading_cache:
                    heading_cache[target] = headings(target)
                if unquote(parsed.fragment) not in heading_cache[target]:
                    errors.append(f'{rel}: missing heading anchor: {link}')
    for path in svg_files:
        rel = path.relative_to(root).as_posix()
        try:
            svg = ET.parse(path).getroot()
        except ET.ParseError as exc:
            errors.append(f'{rel}: invalid XML: {exc}')
            continue
        tag = lambda el: el.tag.rsplit('}', 1)[-1]
        if tag(svg) != 'svg' or svg.attrib.get('role') != 'img':
            errors.append(f'{rel}: SVG must have role="img"')
        ids = {el.attrib['id']: el for el in svg.iter() if 'id' in el.attrib}
        labelled = svg.attrib.get('aria-labelledby', '').split()
        if not labelled or any(key not in ids for key in labelled):
            errors.append(f'{rel}: accessible SVG labels are absent or unresolved')
        for required in ('title', 'desc'):
            if not any(tag(el) == required and ''.join(el.itertext()).strip() for el in svg):
                errors.append(f'{rel}: SVG missing nonempty {required}')
        for el in svg.iter():
            if tag(el) in {'script', 'foreignObject', 'image'}:
                errors.append(f'{rel}: forbidden external/scriptable element: {tag(el)}')
            for key, value in el.attrib.items():
                attr = key.rsplit('}', 1)[-1].lower()
                if attr.startswith('on') or (attr == 'href' and not value.startswith('#')):
                    errors.append(f'{rel}: unsafe or external SVG attribute: {attr}')
                if re.search(r'url\(\s*["\']?(?:https?:|//|data:)', value, re.I):
                    errors.append(f'{rel}: external SVG dependency')
    result = {'result': 'FAIL' if errors else 'PASS', 'scope': 'Offline relative files, Markdown heading anchors, image alt labels and SVG structure only; not live web/source verification.', 'counts': {'markdown_files': len(md_files), 'links': links, 'heading_links': anchors, 'image_embeds': images, 'svg_files': len(svg_files)}, 'errors': errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
