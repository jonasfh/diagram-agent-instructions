#!/usr/bin/env python3
"""Self-bootstrapping helper for Python `diagrams` venv and Graphviz (`dot`)."""

import shutil
import subprocess
import sys
import venv
from pathlib import Path

CACHE_VENV_DIR = Path.home() / ".cache" / "diagram-agent-tools" / "venv"


def ensure_graphviz() -> str:
    """Return path to `dot` binary or raise a clear installation error."""
    dot = shutil.which("dot")
    if dot:
        return dot
    raise RuntimeError(
        "Graphviz (`dot`) is not installed on PATH. Install it first:\n"
        "  Debian/Ubuntu: sudo apt-get update && sudo apt-get install -y --no-install-recommends graphviz\n"
        "  macOS:         brew install graphviz"
    )


def ensure_diagrams_python() -> str:
    """Return path to a Python interpreter that has `diagrams` installed."""
    check = subprocess.run(
        [sys.executable, "-c", "import diagrams"],
        capture_output=True,
        text=True,
    )
    if check.returncode == 0:
        return sys.executable

    venv_python = CACHE_VENV_DIR / "bin" / "python"
    if venv_python.is_file():
        vcheck = subprocess.run(
            [str(venv_python), "-c", "import diagrams"],
            capture_output=True,
            text=True,
        )
        if vcheck.returncode == 0:
            return str(venv_python)

    CACHE_VENV_DIR.parent.mkdir(parents=True, exist_ok=True)
    if not venv_python.is_file():
        venv.create(CACHE_VENV_DIR, with_pip=True)

    subprocess.run(
        [str(venv_python), "-m", "pip", "install", "--quiet", "--disable-pip-version-check", "diagrams"],
        check=True,
    )
    return str(venv_python)


if __name__ == "__main__":
    ensure_graphviz()
    print(ensure_diagrams_python())
