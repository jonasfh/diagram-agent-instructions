---
name: python-diagrams
description: Generates cloud and infrastructure topology diagrams (especially Azure, Kubernetes, and hybrid architectures) using Python's mingrammer/diagrams library with SVG-first output.
---

# Python `diagrams` Skill (`mingrammer/diagrams`)

Use this skill for **cloud and infrastructure topologies**—especially **Azure** landing zones, VNet/subnet boundaries, Kubernetes clusters, and hybrid on-prem architectures—where official cloud provider icons and `Cluster` grouping shine.

## Workflow

1. **Choose Icons** (see `references/azure-icons.md`):
   - Use `diagrams.azure.*` for Azure services, `diagrams.k8s.*` for Kubernetes, `diagrams.onprem.*` for databases/servers/proxies, and `diagrams.custom.Custom` for third-party vendors.
   - Note: `diagrams.custom.Custom` requires a raster image (`.png`); if you only have a `.svg` logo, convert it or use **D2** instead for SVG-native vendor icons.
2. **Author `.py` Script**:
   - Place source files in `docs/diagrams/src/<name>.py`.
   - Always pass `outformat="svg"` and `show=False` to `Diagram(...)`, and set `filename` to output into `docs/diagrams/out/<name>` (without extension).
3. **Render via `render_py_diagram.py`**:
   ```bash
   python3 <path-to-skill>/scripts/render_py_diagram.py docs/diagrams/src/<name>.py
   ```
   - `render_py_diagram.py` bootstraps an isolated venv with `diagrams` in `~/.cache/diagram-agent-tools/venv` and verifies that `dot` (Graphviz) is installed.
   - If `dot` (Graphviz) is missing, follow `SETUP.md` (`sudo apt-get update && sudo apt-get install -y --no-install-recommends graphviz` on Debian/Ubuntu, or `brew install graphviz` on macOS) and re-run.
4. **Verify**:
   - Confirm the `.svg` file was generated and visually inspect it for label overlap, edge routing, and icon clarity.
