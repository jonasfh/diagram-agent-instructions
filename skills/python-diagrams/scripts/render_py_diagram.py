#!/usr/bin/env python3
"""Execute a Python `diagrams` script using auto-bootstrapped venv + Graphviz check."""

import argparse
import base64
import os
import re
import subprocess
import sys
from pathlib import Path

from ensure_tools import ensure_diagrams_python, ensure_graphviz

HREF_PATTERN = re.compile(r'(xlink:href|href)="(/[^"]+\.(?:png|jpg|jpeg|svg))"', re.IGNORECASE)


def _mime_for_ext(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == ".svg":
        return "image/svg+xml"
    if ext in {".jpg", ".jpeg"}:
        return "image/jpeg"
    return "image/png"


def inline_local_images_in_svg(svg_path: Path) -> int:
    """Replace local filesystem image hrefs in an SVG with base64 data URIs."""
    content = svg_path.read_text(encoding="utf-8")
    replaced = 0

    def _replace(match: re.Match[str]) -> str:
        nonlocal replaced
        attr, raw_file = match.group(1), match.group(2)
        img_path = Path(raw_file)
        if not img_path.is_file():
            return match.group(0)
        b64 = base64.b64encode(img_path.read_bytes()).decode("ascii")
        mime = _mime_for_ext(img_path)
        replaced += 1
        return f'{attr}="data:{mime};base64,{b64}"'

    updated = HREF_PATTERN.sub(_replace, content)
    if replaced > 0:
        svg_path.write_text(updated, encoding="utf-8")
    return replaced


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a Python `diagrams` script.")
    parser.add_argument("script", type=Path, help="Path to the .py diagram script")
    parser.add_argument(
        "--cwd",
        type=Path,
        default=None,
        help="Optional working directory (defaults to current working directory)",
    )
    args = parser.parse_args()

    if not args.script.is_file():
        print(f"Error: Script not found: {args.script}", file=sys.stderr)
        return 1

    try:
        ensure_graphviz()
        py_bin = ensure_diagrams_python()
    except Exception as exc:
        print(f"Tool setup error:\n{exc}", file=sys.stderr)
        return 1

    env = os.environ.copy()
    cwd = str(args.cwd) if args.cwd else os.getcwd()
    result = subprocess.run([py_bin, str(args.script.resolve())], cwd=cwd, env=env, capture_output=True, text=True)

    if result.returncode != 0:
        print("Python diagram execution failed:", file=sys.stderr)
        if result.stderr:
            print(result.stderr.strip(), file=sys.stderr)
        if result.stdout:
            print(result.stdout.strip(), file=sys.stderr)
        return result.returncode

    search_roots = {Path(cwd), args.script.resolve().parent, args.script.resolve().parents[1] / "out"}
    inlined_files = 0
    for root in search_roots:
        if root.is_dir():
            for svg_file in root.glob("*.svg"):
                if inline_local_images_in_svg(svg_file) > 0:
                    inlined_files += 1

    if result.stdout.strip():
        print(result.stdout.strip())
    print(f"Successfully executed diagram script: {args.script} (inlined icons in {inlined_files} SVG file(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
