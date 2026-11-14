#!/usr/bin/env python3
"""Execute a Python `diagrams` script using auto-bootstrapped venv + Graphviz check."""

import argparse
import os
import subprocess
import sys
from pathlib import Path

from ensure_tools import ensure_diagrams_python, ensure_graphviz


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

    if result.stdout.strip():
        print(result.stdout.strip())
    print(f"Successfully executed diagram script: {args.script}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
