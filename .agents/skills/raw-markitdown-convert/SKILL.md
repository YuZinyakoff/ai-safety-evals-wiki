---
name: raw-markitdown-convert
description: Convert PDF and other MarkItDown-supported documents under raw/ into adjacent Markdown sidecars without touching wiki/. Use when the user wants repo-local conversion helpers for raw source files, bulk conversion under raw/, or a safe workflow that writes filename.ext.md next to the original file.
---

# Raw MarkItDown Convert

Use this skill when the task is to create or run a repo-local conversion workflow that:

- reads files only from `raw/`
- converts them with MarkItDown
- writes Markdown sidecars next to the originals
- never modifies `wiki/`

## What this skill provides

- A script at `.agents/skills/raw-markitdown-convert/convert_raw_with_markitdown.py`
- Safe path checks that reject targets outside `raw/`
- Sidecar output naming `filename.ext.md` by default to avoid clobbering existing `.md` files

## Default workflow

1. Confirm the target is inside `raw/`.
2. Run a dry-run first:

```bash
python3 .agents/skills/raw-markitdown-convert/convert_raw_with_markitdown.py raw --dry-run
```

3. Convert a subtree or a single file:

```bash
python3 .agents/skills/raw-markitdown-convert/convert_raw_with_markitdown.py raw/week-02
python3 .agents/skills/raw-markitdown-convert/convert_raw_with_markitdown.py "raw/week-02/theory/2411.00640v1.pdf"
```

## Behavior

- The script skips Markdown files and notebooks.
- The script skips existing sidecars unless `--force` is used.
- The default output path is `original_name.ext.md`.
- Use `--replace-extension` only when you explicitly want `original_name.md`.

## MarkItDown dependency

The script expects the Python package `markitdown` to be installed. The official repo documents:

- repo default for this repository: `pip install 'markitdown[pdf]'`
- broader install when more formats appear: `pip install 'markitdown[all]'`
- Python API pattern: `MarkItDown().convert(path).text_content`

If the import fails, the script exits with a clear error and does nothing.

Official reference:
- https://github.com/microsoft/markitdown
