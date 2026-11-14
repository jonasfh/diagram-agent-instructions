# Tool Setup & Self-Bootstrapping Guide (For AI Agents)

This repository uses **self-bootstrapping** so diagramming works across projects without requiring manual `Dockerfile` edits.

## 1. D2 (`d2-diagrams/scripts/render_d2.py`)

- `render_d2.py` calls `ensure_tools.py`, which checks `PATH` for `d2` and otherwise downloads the latest official static binary for the current OS/architecture into `~/.cache/diagram-agent-tools/bin/d2`.
- **No root/sudo required.**

## 2. Python `diagrams` + Graphviz (`python-diagrams/scripts/render_py_diagram.py`)

- `render_py_diagram.py` calls `ensure_tools.py`, which:
  1. Checks if `diagrams` is importable in the active Python or creates an isolated venv at `~/.cache/diagram-agent-tools/venv` with `diagrams` installed.
  2. Checks if `dot` (Graphviz) is on `PATH`.
- **If `dot` is missing**:
  - On Debian/Ubuntu Linux:
    ```bash
    sudo apt-get update && sudo apt-get install -y --no-install-recommends graphviz
    ```
  - On macOS:
    ```bash
    brew install graphviz
    ```
  - If `sudo` is unavailable and `dot` is missing, report the missing system dependency clearly to the user and use D2 (`--layout=elk`) as an alternative if appropriate.
