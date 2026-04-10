#!/usr/bin/env python3
"""Convert supported raw/ documents into adjacent Markdown sidecars via MarkItDown."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable


SKIP_SUFFIXES = {
    ".md",
    ".markdown",
    ".ipynb",
}

SUPPORTED_SUFFIXES = {
    ".pdf",
    ".pptx",
    ".docx",
    ".xlsx",
    ".xls",
    ".msg",
    ".html",
    ".htm",
    ".csv",
    ".json",
    ".xml",
    ".zip",
    ".epub",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".tif",
    ".webp",
    ".wav",
    ".mp3",
    ".m4a",
}


def find_repo_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "raw").is_dir() and (candidate / "wiki").is_dir():
            return candidate
    raise RuntimeError("Could not find repository root containing raw/ and wiki/")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Convert files under raw/ into adjacent Markdown sidecars using MarkItDown. "
            "By default writes filename.ext.md and skips existing sidecars."
        )
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["raw"],
        help="One or more files or directories inside raw/. Default: raw",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned conversions without writing files.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing sidecar Markdown files.",
    )
    parser.add_argument(
        "--replace-extension",
        action="store_true",
        help="Write original_name.md instead of original_name.ext.md.",
    )
    parser.add_argument(
        "--use-plugins",
        action="store_true",
        help="Enable MarkItDown plugins.",
    )
    return parser.parse_args(argv)


def ensure_inside_raw(path: Path, raw_root: Path) -> Path:
    resolved = path.resolve()
    try:
        resolved.relative_to(raw_root)
    except ValueError as exc:
        raise ValueError(f"Path is outside raw/: {path}") from exc
    return resolved


def iter_candidates(paths: Iterable[Path], raw_root: Path) -> Iterable[Path]:
    seen: set[Path] = set()
    for path in paths:
        resolved = ensure_inside_raw(path, raw_root)
        if resolved.is_dir():
            for child in sorted(resolved.rglob("*")):
                if not child.is_file():
                    continue
                if child in seen:
                    continue
                seen.add(child)
                if is_supported_candidate(child):
                    yield child
            continue

        if resolved.is_file() and resolved not in seen:
            seen.add(resolved)
            if is_supported_candidate(resolved):
                yield resolved


def is_supported_candidate(path: Path) -> bool:
    lower_name = path.name.lower()
    if lower_name.endswith(".md") or lower_name.endswith(".markdown"):
        return False
    if path.suffix.lower() in SKIP_SUFFIXES:
        return False
    return path.suffix.lower() in SUPPORTED_SUFFIXES


def sidecar_path(path: Path, replace_extension: bool) -> Path:
    if replace_extension:
        return path.with_suffix(".md")
    return path.with_name(path.name + ".md")


def load_markitdown(enable_plugins: bool):
    try:
        from markitdown import MarkItDown
    except ImportError as exc:
        raise SystemExit(
            "MarkItDown is not installed. Install it first with the extras you need, for example:\n"
            "  pip install 'markitdown[pdf]'"
        ) from exc
    return MarkItDown(enable_plugins=enable_plugins)


def convert_file(converter, source: Path, destination: Path, dry_run: bool) -> str:
    if dry_run:
        return "planned"
    result = converter.convert(str(source))
    destination.write_text(result.text_content, encoding="utf-8")
    return "written"


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    repo_root = find_repo_root(Path(__file__).resolve())
    raw_root = (repo_root / "raw").resolve()

    requested_paths = []
    for item in args.paths:
        candidate = Path(item)
        if not candidate.is_absolute():
            candidate = repo_root / candidate
        if not candidate.exists():
            print(f"missing: {item}", file=sys.stderr)
            return 2
        requested_paths.append(candidate)

    candidates = list(iter_candidates(requested_paths, raw_root))
    if not candidates:
        print("No supported files found under raw/.")
        return 0

    converter = None if args.dry_run else load_markitdown(enable_plugins=args.use_plugins)

    written = 0
    skipped = 0
    failed = 0

    for source in candidates:
        destination = sidecar_path(source, replace_extension=args.replace_extension)
        if destination.exists() and not args.force:
            print(f"skip existing: {destination.relative_to(repo_root)}")
            skipped += 1
            continue
        try:
            status = convert_file(converter, source, destination, dry_run=args.dry_run)
            print(
                f"{status}: {source.relative_to(repo_root)} -> "
                f"{destination.relative_to(repo_root)}"
            )
            written += 1
        except Exception as exc:  # pragma: no cover - runtime integration path
            print(f"fail: {source.relative_to(repo_root)} ({exc})", file=sys.stderr)
            failed += 1

    print(
        f"summary: candidates={len(candidates)} written={written} "
        f"skipped={skipped} failed={failed}"
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
