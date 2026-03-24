#!/usr/bin/env python3
"""
Build docs/index.html from README.md.
README.md is the single source of truth — run this after any edits.
"""

import html as html_module
import subprocess
import re
from pathlib import Path

MD  = "README.md"
OUT = "docs/index.html"

# ── Read source ──────────────────────────────────────────────────────────────
text = Path(MD).read_text(encoding="utf-8")

# Extract "Last updated" timestamp
ts_match = re.search(r'Last updated: ([\d-]+ \d{4} CST)', text)
timestamp = ts_match.group(1) if ts_match else ""

# ── Extract body ─────────────────────────────────────────────────────────────
# Skip: top-level h1 title, *Last updated* lines (appear at top and bottom).
# Keep everything else: intro paragraph, contributing notice, TOC, all sections.
lines = text.split('\n')
body_lines = []
in_body = False
for line in lines:
    if re.match(r'^# ', line):              # skip h1 title (goes in template)
        continue
    if re.match(r'^\*Last updated', line):  # skip timestamp lines
        continue
    if not in_body and line.strip() == '':  # skip leading blank lines
        continue
    in_body = True
    body_lines.append(line)

body_md = '\n'.join(body_lines).rstrip()

# Fix GitHub-relative links so they work in the standalone HTML file
body_md = body_md.replace(
    '../../issues',
    'https://github.com/juren53/Dwarf-Mini-FAQ/issues'
)
body_md = body_md.replace(
    '](CONTRIBUTING.md)',
    '](https://github.com/juren53/Dwarf-Mini-FAQ/blob/master/CONTRIBUTING.md)'
)

# ── Convert to HTML via pandoc ───────────────────────────────────────────────
result = subprocess.run(
    ['pandoc', '--from', 'markdown+smart', '--to', 'html'],
    input=body_md.encode('utf-8'), capture_output=True, check=True
)
body_html = result.stdout.decode('utf-8').strip()

# ── Fix heading IDs to match GitHub-style anchors used in the TOC ────────────
# Pandoc strips leading "N. " from IDs and handles & differently from GitHub.
# GitHub's scheme: lowercase, spaces→hyphens, remove non-[a-z0-9-].
# This makes the TOC links (written for GitHub) work in the HTML too.
def github_id(heading_text):
    text = heading_text.lower()
    text = re.sub(r'\s+', '-', text)   # all whitespace (incl. newlines) → hyphen
    text = re.sub(r'[^a-z0-9-]', '', text)
    return text

def fix_heading_ids(h):
    def replacer(m):
        tag     = m.group(1)          # e.g. h2
        content = m.group(2)          # inner HTML of the heading
        plain   = html_module.unescape(re.sub(r'<[^>]+>', '', content))
        new_id  = github_id(plain)
        return f'<{tag} id="{new_id}">{content}</{tag}>'
    return re.sub(r'<(h[2-6])[^>]*>(.*?)</\1>', replacer, h, flags=re.DOTALL)

body_html = fix_heading_ids(body_html)

# Indent every line by two spaces to match the surrounding HTML
body_html = '\n'.join(
    ('  ' + line) if line else ''
    for line in body_html.split('\n')
)

# ── Assemble full HTML ───────────────────────────────────────────────────────
html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dwarf Mini Smart Telescope &#8212; FAQ</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">

  <h1>Dwarf Mini Smart Telescope &#8212; FAQ</h1>

{body_html}

  <p class="timestamp"><em>Last updated: {timestamp}</em></p>

</div>
</body>
</html>
'''

Path(OUT).parent.mkdir(exist_ok=True)
Path(OUT).write_text(html, encoding="utf-8")
print(f"HTML written to {OUT}")
