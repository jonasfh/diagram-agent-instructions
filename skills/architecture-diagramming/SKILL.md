---
name: architecture-diagramming
description: Orchestrates technical, architecture, workflow, and infrastructure diagramming by analyzing the codebase, selecting the best tool (Mermaid, D2, or Python diagrams), enforcing SVG-first output, and visually verifying the rendered result.
---

# Architecture Diagramming Orchestrator

Use this skill whenever the user asks for an architecture diagram, system overview, integration flow, deployment topology, or workflow diagram.

## Workflow

1. **Analyze the Codebase First**:
   - Inspect actual entry points, services, APIs, queues, databases, and external integrations before drawing anything. Never invent components.
2. **Select the Right Tool** (see `references/tool-selection-matrix.md`):
   - **Mermaid** (`mermaid-diagrams` skill): Simple inline Markdown diagrams (`< 10` nodes), `erDiagram` schemas, or small sequence diagrams inside `README.md` / PR descriptions.
   - **D2** (`d2-diagrams` skill): Complex system architectures, layered applications, integration flows, and workflows requiring clean orthogonal routing (`--layout=elk`) and vendor SVG icons.
   - **Python `diagrams`** (`python-diagrams` skill): Cloud & infrastructure topologies (especially **Azure**, Kubernetes, VNet/hybrid) where official cloud provider icons and `Cluster` boundaries are essential.
3. **Apply Layout & Aesthetic Rules** (see `references/layout-and-aesthetics.md`):
   - Keep each diagram focused (`<= 12-15` nodes). Split into an overview diagram plus detail diagrams if the system is larger.
   - Use consistent flow direction (`right` or `down`), explicit container boundaries, and concise edge labels (protocol, event, or action).
4. **Render & Visually Verify**:
   - Output **SVG** by default (`docs/diagrams/src/` -> `docs/diagrams/out/`).
   - Run the skill's render script (`render_d2.py` or `render_py_diagram.py`), fix any errors, and visually inspect the rendered output for overlapping labels, clipped boxes, or messy routing before finishing.
5. **Sync Documentation**:
   - Embed or link the rendered `.svg` in `DEV_README.md` / `README.md` / `docs/` as appropriate.
