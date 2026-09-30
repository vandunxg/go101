#!/usr/bin/env python3
"""Report English/vi translation coverage and upstream drift."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "pages"
VI_ROOT = ROOT / "translations" / "vi" / "pages"
STATE_PATH = ROOT / "translations" / "vi" / ".sync-state.json"


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def load_state() -> dict[str, str]:
    if not STATE_PATH.exists():
        return {}
    data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in data.items()):
        raise ValueError(f"invalid state file: {STATE_PATH}")
    return data


def source_pages() -> dict[str, Path]:
    pages: dict[str, Path] = {}
    for path in SOURCE_ROOT.rglob("*.tmd"):
        pages[path.relative_to(ROOT).as_posix()] = path
    for path in SOURCE_ROOT.rglob("*.html"):
        # The .html files generated from .tmd are handled through their .tmd source.
        relative = path.relative_to(ROOT).as_posix()
        if not path.with_suffix(".tmd").exists():
            pages[relative] = path
    return pages


def translation_sources() -> dict[str, Path]:
    if not VI_ROOT.exists():
        return {}
    pages = {"pages/" + path.relative_to(VI_ROOT).as_posix(): path for path in VI_ROOT.rglob("*.tmd")}
    for path in VI_ROOT.rglob("*.html"):
        if not path.with_suffix(".tmd").exists():
            pages["pages/" + path.relative_to(VI_ROOT).as_posix()] = path
    return pages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mark-reviewed", metavar="SOURCE_PATH", help="record the current source SHA after reviewing its translation")
    args = parser.parse_args()

    try:
        state = load_state()
        sources = source_pages()
        translations = translation_sources()
        if args.mark_reviewed:
            relative_path = Path(args.mark_reviewed)
            relative = relative_path.as_posix()
            source = ROOT / relative
            translated = ROOT / "translations" / "vi" / relative
            if relative_path.is_absolute() or ".." in relative_path.parts or not source.is_file() or not source.resolve().is_relative_to(SOURCE_ROOT.resolve()):
                print(f"Not an English page under pages/: {relative}", file=sys.stderr)
                return 2
            if not translated.is_file() or not translated.resolve().is_relative_to((ROOT / "translations" / "vi").resolve()):
                print(f"Translation not found: {translated.relative_to(ROOT)}", file=sys.stderr)
                return 2
            state[relative] = git_blob_sha(source)
            STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"Recorded reviewed source: {relative}")
            return 0

        missing: list[str] = []
        stale: list[str] = []
        untracked: list[str] = []
        current: list[str] = []
        orphan: list[str] = []

        for relative, source in sorted(sources.items()):
            translated = translations.get(relative)
            if translated is None:
                missing.append(relative)
                continue
            recorded = state.get(relative)
            if recorded is None:
                untracked.append(relative)
            elif recorded != git_blob_sha(source):
                stale.append(relative)
            else:
                current.append(relative)

        for relative in sorted(set(translations) - set(sources)):
            orphan.append(relative)

        print(f"Current: {len(current)} | Stale: {len(stale)} | Untracked review: {len(untracked)} | Missing: {len(missing)} | Orphan: {len(orphan)}")
        for label, rows in (("Stale", stale), ("Untracked review", untracked), ("Orphan", orphan), ("Missing", missing)):
            if rows:
                print(f"\n{label}:")
                for row in rows:
                    print(f"  {row}")
        # Missing pages are expected while the translation project is in progress.
        return 1 if stale or untracked or orphan else 0
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(error, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
