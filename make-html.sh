#!/bin/bash
# Generate docs/index.html from FAQ_Dwarf-Mini-Telescope.md.
# FAQ_Dwarf-Mini-Telescope.md is the single source of truth — run this after any edits.

set -e

cd "$(dirname "$0")"
export PATH="$PATH:/c/Program Files/Pandoc"
python build-html.py
