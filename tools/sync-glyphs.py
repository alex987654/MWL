#!/usr/bin/env python3
"""Regenerate the MWL symbol sprite from the standalone glyph files.

MWL-glyphs/*.svg is the single source of truth. This script converts each file
into a palette-parameterized <symbol id="MWL-icon-NAME"> (hex colors become
var(--colorN, #hex), driven by the palette in the hosts' <style> blocks) and
splices the full symbol block into every file that embeds it:

    MWL-symbol-defs/symbol-defs.svg
    MWL-symbol-defs/demo.html        (also gets a demo tile per glyph)
    Star-Wars-4-Crawl-in-MWL.html
    The-Twin-Exodus-MWL-Sample.html

Missing --colorN palette entries are appended to each host's
`.default-palette, .palette0 { ... }` rule. Run from the repo root:

    python3 tools/sync-glyphs.py
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLYPH_DIR = os.path.join(ROOT, 'MWL-glyphs')
HOSTS = [
    'MWL-symbol-defs/symbol-defs.svg',
    'MWL-symbol-defs/demo.html',
    'Star-Wars-4-Crawl-in-MWL.html',
    'The-Twin-Exodus-MWL-Sample.html',
]
DROP_ATTRS = {'xmlns', 'xmlns:xlink', 'width', 'height', 'xml:space'}


def canon(hexcolor):
    h = hexcolor.lower()
    if len(h) == 4:  # #abc -> #aabbcc
        h = '#' + ''.join(c * 2 for c in h[1:])
    return h


def parse_palette(text):
    """hex -> var name, from --colorN: #hex; declarations."""
    palette, top = {}, -1
    for n, h in re.findall(r'--color(\d+)\s*:\s*(#[0-9a-fA-F]{3,6})\s*;', text):
        top = max(top, int(n))
        palette.setdefault(canon(h), f'--color{n}')
    return palette, top


def load_symbols(palette, next_idx):
    """Build all <symbol> blocks; returns (stems, block_text, new_palette_entries)."""
    new_entries = {}

    def var_for(h):
        nonlocal next_idx
        ch = canon(h)
        if ch not in palette:
            name = f'--color{next_idx}'
            next_idx += 1
            palette[ch] = name
            new_entries[name] = ch
        return palette[ch]

    def colorize(content):
        content = re.sub(
            r'(fill|stroke|stop-color)="(#[0-9a-fA-F]{3,6})"',
            lambda m: f'{m.group(1)}="var({var_for(m.group(2))}, {canon(m.group(2))})"',
            content)
        content = re.sub(
            r'(fill|stroke|stop-color)\s*:\s*(#[0-9a-fA-F]{3,6})',
            lambda m: f'{m.group(1)}:var({var_for(m.group(2))}, {canon(m.group(2))})',
            content)
        return content

    stems, blocks = [], []
    for path in sorted(glob.glob(os.path.join(GLYPH_DIR, '*.svg'))):
        stem = os.path.basename(path)[:-4]
        stems.append(stem)
        src = open(path).read()
        m = re.search(r'<svg\b([^>]*)>', src)
        attrs = []
        for am in re.finditer(r'([\w:-]+)="([^"]*)"', m.group(1)):
            if am.group(1) not in DROP_ATTRS and am.group(1) != 'viewBox':
                attrs.append(f'{am.group(1)}="{am.group(2)}"')
        inner = src[m.end():src.rindex('</svg>')].strip()
        inner = colorize(inner)
        inner = '\n'.join('            ' + ln.strip() for ln in inner.splitlines() if ln.strip())
        attr_str = (' ' + ' '.join(attrs)) if attrs else ''
        blocks.append(
            f'        <symbol id="MWL-icon-{stem}" viewBox="0 0 512 512"{attr_str}>\n'
            f'            <title>{stem}</title>\n'
            f'{inner}\n'
            f'        </symbol>')
    return stems, '\n'.join(blocks), new_entries


def patch_palette(text, new_entries):
    if not new_entries:
        return text
    m = re.search(r'(\.default-palette\s*,\s*\.palette0\s*\{)([^}]*)(\})', text)
    if not m:
        return text
    body = m.group(2)
    indent = re.search(r'\n(\s*)--color', body)
    pad = indent.group(1) if indent else '            '
    add = ''.join(f'{pad}{name}: {h};\n' for name, h in sorted(
        new_entries.items(), key=lambda kv: int(kv[0][7:])))
    return text[:m.end(2)].rstrip('\n') + '\n' + add + pad[:-4] + '}' + text[m.end(3):]


def splice_symbols(text, block):
    start = text.index('<symbol')
    start = text.rindex('\n', 0, start) + 1
    end = text.rindex('</symbol>') + len('</symbol>')
    return text[:start] + block + text[end:]


def patch_demo_tiles(text, stems):
    tile = ('            <div class="centered _demo_glyph"><svg width="128" height="128" '
            'class="default-palette"><use href="#MWL-icon-{s}" /></svg>'
            '<span class="overflowEllipsis">MWL-icon-{s}</span></div>')
    existing = re.findall(r'_demo_glyph"><svg[^>]*><use href="#MWL-icon-([^"]+)"', text)
    if not existing:
        return text, 0
    added = 0
    for stem in stems:
        if stem in existing:
            continue
        # insert alphabetically among existing tiles
        after = None
        for e in sorted(existing):
            if e < stem:
                after = e
        if after is None:
            anchor = re.search(r'[ \t]*<div class="centered _demo_glyph">.*?MWL-icon-'
                               + re.escape(sorted(existing)[0]), text).start()
            insert_at = text.rindex('\n', 0, anchor) + 1
            text = text[:insert_at] + tile.format(s=stem) + '\n' + text[insert_at:]
        else:
            pat = re.search(r'[ \t]*<div class="centered _demo_glyph"><svg[^>]*>'
                            r'<use href="#MWL-icon-' + re.escape(after) + r'" />.*?</div>', text)
            insert_at = pat.end()
            text = text[:insert_at] + '\n' + tile.format(s=stem) + text[insert_at:]
        existing.append(stem)
        added += 1
    return text, added


def main():
    master = open(os.path.join(ROOT, HOSTS[0])).read()
    palette, top = parse_palette(master)
    stems, block, new_entries = load_symbols(palette, top + 1)
    print(f'{len(stems)} glyphs; {len(new_entries)} new palette colors: '
          + (', '.join(f'{k}={v}' for k, v in new_entries.items()) or '-'))
    for rel in HOSTS:
        path = os.path.join(ROOT, rel)
        text = open(path).read()
        before = len(re.findall(r'<symbol ', text))
        text = splice_symbols(text, block)
        text = patch_palette(text, new_entries)
        note = ''
        if rel.endswith('demo.html'):
            text, added = patch_demo_tiles(text, stems)
            note = f', +{added} demo tiles'
        open(path, 'w').write(text)
        print(f'  {rel}: {before} -> {len(stems)} symbols{note}')


if __name__ == '__main__':
    sys.exit(main())
