#!/usr/bin/env python3
"""Compile a .d2 diagram to SVG (default) or PNG using auto-bootstrapped d2 CLI."""

import argparse
import subprocess
import sys
from pathlib import Path

from ensure_tools import ensure_d2


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a D2 diagram to SVG or PNG.")
    parser.add_argument("input", type=Path, help="Path to source .d2 file")
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        help="Output path (.svg or .png). Defaults to input stem with .svg.",
    )
    parser.add_argument(
        "--layout",
        default="elk",
        choices=["elk", "dagre", "tala"],
        help="D2 layout engine (default: elk)",
    )
    parser.add_argument(
        "--theme",
        type=int,
        default=0,
        help="D2 theme ID (default: 0 - Neutral Default)",
    )
    parser.add_argument(
        "--pad",
        type=int,
        default=40,
        help="Padding around diagram in px (default: 40)",
    )
    args = parser.parse_args()

    if not args.input.is_file():
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        return 1

    output_path = args.output or args.input.with_suffix(".svg")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        d2_bin = ensure_d2()
    except Exception as exc:
        print(f"Error bootstrapping d2 CLI: {exc}", file=sys.stderr)
        return 1

    cmd = [
        d2_bin,
        f"--layout={args.layout}",
        f"--theme={args.theme}",
        f"--pad={args.pad}",
        str(args.input),
        str(output_path),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("D2 compilation failed:", file=sys.stderr)
        if result.stderr:
            print(result.stderr.strip(), file=sys.stderr)
        if result.stdout:
            print(result.stdout.strip(), file=sys.stderr)
        return result.returncode

    print(f"Rendered D2 diagram: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
