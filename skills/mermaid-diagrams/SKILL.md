---
name: mermaid-diagrams
description: Generates clean, high-contrast Mermaid diagrams for inline Markdown documentation (README.md, DEV_README.md, PRs), erDiagram schemas, and small sequence/flow diagrams.
---

# Mermaid Diagrams Skill

Use Mermaid *only* for lightweight diagrams embedded directly in Markdown (`README.md`, `DEV_README.md`, PR descriptions), `erDiagram` database schemas, and small flows/sequences (`< 10` nodes). For complex architectures or vendor icons, use **D2** (`d2-diagrams`) or **Python `diagrams`** (`python-diagrams`).

## Rules

1. **Keep it Small**: Limit flowcharts to `< 10` nodes. Switch to D2 when layouts become cramped or edges cross excessively.
2. **Light & Dark Mode Contrast**: Use explicit `classDef` fills with mid-tone borders and dark readable text (or GitHub-safe neutral palettes).
3. **`erDiagram` Hygiene**:
   - Write each relationship declaration on a **single physical line**.
   - Never use tabs; use spaces.
   - Prefer simple ASCII relationship labels (`contains`, `belongs_to`, `has_many`, `references`).
4. **References**: See `references/mermaid-templates.md` for copy-ready templates.
