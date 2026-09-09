#!/usr/bin/env python3
"""Update license years across a repository.

Usage: python update_license_year.py --root . --year 2026 --dry-run
"""
import argparse
import os
import re
from pathlib import Path

text_file_extensions = None

EXCLUDE_DIRS = {".git", "node_modules", "dist", "build", "venv", "__pycache__"}

COPYRIGHT_RANGE_RE = re.compile(r'(Copyright[^\n\r]{0,120}?)(20\d{2})(?:-(20\d{2}))?', re.IGNORECASE)
COPYRIGHT_SYMBOL_RE = re.compile(r'(©\s*)(20\d{2})(?:-(20\d{2}))?', re.IGNORECASE)

def is_text_file(path: Path) -> bool:
    try:
        with path.open('rb') as f:
            chunk = f.read(4096)
            if b"\0" in chunk:
                return False
    except Exception:
        return False
    return True


def process_file(path: Path, target_year: str) -> int:
    try:
        text = path.read_text(encoding='utf-8')
    except Exception:
        try:
            text = path.read_text(encoding='latin-1')
        except Exception:
            return 0

    changed = 0

    def repl_range(m):
        nonlocal changed
        prefix = m.group(1)
        start = m.group(2)
        end = m.group(3)
        if end:
            if end == target_year:
                return m.group(0)
            changed += 1
            return f"{prefix}{start}-{target_year}"
        else:
            if start == target_year:
                return m.group(0)
            changed += 1
            return f"{prefix}{target_year}"

    new_text = COPYRIGHT_RANGE_RE.sub(repl_range, text)

    def repl_symbol(m):
        nonlocal changed
        prefix = m.group(1)
        start = m.group(2)
        end = m.group(3)
        if end:
            if end == target_year:
                return m.group(0)
            changed += 1
            return f"{prefix}{start}-{target_year}"
        else:
            if start == target_year:
                return m.group(0)
            changed += 1
            return f"{prefix}{target_year}"

    new_text = COPYRIGHT_SYMBOL_RE.sub(repl_symbol, new_text)

    if changed > 0 and new_text != text:
        return changed, new_text
    return 0, None


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--root', default='.', help='Repository root to scan')
    p.add_argument('--year', type=str, default=str(__import__('datetime').datetime.now().year), help='Target year')
    p.add_argument('--dry-run', action='store_true')
    args = p.parse_args()

    root = Path(args.root)
    if not root.exists():
        print('Root not found:', root)
        return 2

    total_files = 0
    total_changes = 0
    changed_files = []

    for dirpath, dirnames, filenames in os.walk(root):
        parts = Path(dirpath).parts
        if any(p in EXCLUDE_DIRS for p in parts):
            continue
        for filename in filenames:
            path = Path(dirpath) / filename
            if path.is_dir():
                continue
            # skip binary files heuristically
            if not is_text_file(path):
                continue
            total_files += 1
            try:
                changed, new_text = process_file(path, args.year)
            except Exception:
                changed = 0
                new_text = None
            if changed:
                total_changes += changed
                changed_files.append((str(path.relative_to(root)), changed))
                if not args.dry_run:
                    # backup
                    try:
                        backup = path.with_suffix(path.suffix + '.bak')
                        if not backup.exists():
                            backup.write_bytes(path.read_bytes())
                    except Exception:
                        pass
                    try:
                        path.write_text(new_text, encoding='utf-8')
                    except Exception:
                        try:
                            path.write_text(new_text, encoding='latin-1')
                        except Exception:
                            print('Failed to write', path)

    print(f'Scanned files: {total_files}')
    print(f'Total replacements: {total_changes}')
    if changed_files:
        print('Files changed:')
        for fn, cnt in changed_files:
            print(f' - {fn}: {cnt} replacement(s)')
    else:
        print('No files changed.')

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
