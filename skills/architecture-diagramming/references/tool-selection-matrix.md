# Tool Selection Matrix

Choose the tool that matches the diagram's complexity, audience, and icon needs:

| Criterion | Mermaid | D2 (`--layout=elk`) | Python `diagrams` |
| :--- | :--- | :--- | :--- |
| **Best For** | Inline Markdown flows, small sequence diagrams, `erDiagram` | Complex system architecture, layered modules, integration flows, workflows | Cloud & infrastructure topologies (Azure, AWS, GCP, K8s, hybrid) |
| **Node / Edge Complexity** | Low (`<= 8-10` nodes) | Medium to High (`10-25+` nodes, nested containers) | Medium (`5-20` nodes grouped in `Cluster`s) |
| **Vendor / Cloud Icons** | Very limited | Strong (Terrastruct icons + any local/downloaded `.svg` icon) | Excellent (built-in official Azure/AWS/GCP/K8s/OnPrem icon packs) |
| **Inline in GitHub Markdown** | Native fenced code block | Linked `.svg` image (`![alt](docs/diagrams/out/name.svg)`) | Linked `.svg` image (`![alt](docs/diagrams/out/name.svg)`) |
| **Default Output Format** | Inline `.md` / `.mmd` | `.svg` (via `render_d2.py`) | `.svg` (via `render_py_diagram.py`) |

## Decision Rules

1. **Need an `erDiagram` or a quick 5-box flow inside `README.md`?** -> Use **Mermaid**.
2. **Building an Azure / Kubernetes / multi-zone cloud infrastructure diagram?** -> Use **Python `diagrams`**.
3. **Building a software architecture, microservice/plugin topology, or multi-step integration workflow (e.g. WordPress + Vipps + Cron + DB)?** -> Use **D2**.
4. **Need a PNG instead of SVG?** -> Only override the SVG-first default when a target viewer/platform fails to render embedded SVG icons or explicitly requires raster.
