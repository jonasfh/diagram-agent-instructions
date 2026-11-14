# Diagram & Architecture Documentation Guidelines

## Core Rules

1. **Choose the Right Tool**:
   - **Mermaid**: Use *only* for simple inline Markdown diagrams (`README.md`, `DEV_README.md`, PRs), small sequence/flow diagrams (< 10 nodes), and `erDiagram` database schemas.
   - **D2 (`--layout=elk`)**: Default choice for complex system architectures, layered component diagrams, integration flows, and workflows with vendor icons.
   - **Python `diagrams`**: Default choice for cloud and infrastructure topologies (Azure, AWS, GCP, Kubernetes, hybrid/on-prem) where official cloud provider icons and cluster boundaries matter.
2. **SVG-First Output**:
   - Always generate `.svg` by default for D2 and Python `diagrams`.
   - Use `.png` only when raster output has clear advantages or a target viewer handles SVG poorly.
3. **Source & Artifact Side-by-Side**:
   - Keep diagram sources (`.d2`, `.py`) and rendered outputs (`.svg`) versioned in Git (recommended layout: `docs/diagrams/src/`, `docs/diagrams/out/`, and `docs/diagrams/assets/icons/`).
4. **Vendor & Provider Icons**:
   - Use Azure icons (`diagrams.azure.*` or Terrastruct/local SVGs) for cloud architectures.
   - For third-party/local vendors (e.g., Vipps, MobilePay, Stripe, WordPress), check `docs/diagrams/assets/icons/` first and download verified SVGs on demand when missing.
5. **Visual Quality & Verification**:
   - Keep each diagram focused (aim for ≤ 12–15 nodes; split overview and detail views when needed).
   - Always compile via the bundled render scripts (`render_d2.py` / `render_py_diagram.py`), fix any errors, and visually inspect the output before finishing.
6. **Continuous Sync**:
   - Update diagrams and their sources in the same PR whenever architecture, endpoints, workflows, or schemas change.
