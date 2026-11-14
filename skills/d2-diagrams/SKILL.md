---
name: d2-diagrams
description: Generates professional, layered architecture and workflow diagrams using the D2 CLI (--layout=elk), SVG-first output, and on-demand vendor SVG icons.
---

# D2 Diagrams Skill

Use this skill for complex system architectures, layered application views, integration flows, and workflows that benefit from clean orthogonal routing (`elk`) and vendor icons.

## Workflow

1. **Prepare Icons** (see `references/icon-workflow.md`):
   - Check `docs/diagrams/assets/icons/` for existing vendor SVGs.
   - Download missing vendor icons (e.g., WordPress, Vipps, MobilePay, Stripe) as verified SVGs into `docs/diagrams/assets/icons/` or use Azure/tech icons from `icons.terrastruct.com` (downloaded locally when offline/self-contained SVGs are preferred).
   - Note: D2 embeds local SVG icons cleanly when referenced with relative paths (e.g. `icon: ../assets/icons/vipps.svg`).
2. **Author `.d2` Source** (see `references/d2-patterns.md`):
   - Place source files in `docs/diagrams/src/<name>.d2`.
   - Use explicit `direction: right` (or `down`), clean container grouping, and concise edge labels.
   - Keep styling restrained with high contrast.
3. **Compile to SVG via `render_d2.py`**:
   ```bash
   python3 <path-to-skill>/scripts/render_d2.py docs/diagrams/src/<name>.d2 docs/diagrams/out/<name>.svg
   ```
   - `render_d2.py` automatically bootstraps `d2` into `~/.cache/diagram-agent-tools/bin/d2` if not already on `PATH`.
   - Default layout engine is `elk`. Override with `--layout dagre` if needed (e.g., for sequence diagrams, use `shape: sequence_diagram` with `dagre`).
   - Default output is **SVG**. Only pass a `.png` output path if raster is explicitly needed.
4. **Verify**:
   - Fix any syntax errors reported by `render_d2.py` and re-run.
   - Inspect the generated SVG (or render a quick PNG preview if needed) to verify icon rendering, spacing, and label legibility.
