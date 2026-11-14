# Layout & Aesthetics Guide

Follow these rules to keep diagrams executive-ready and readable:

1. **One Story per Diagram**:
   - Aim for **<= 12-15 nodes** per diagram. If a system has 30+ components, create a System Context / Overview diagram and separate Detail diagrams.
2. **Consistent Direction**:
   - Use `left-to-right` (`LR` / `direction: right`) for data pipelines, request/integration flows, and layered architectures.
   - Use `top-to-bottom` (`TB` / `direction: down`) for hierarchies, cloud landing zones, and deployment stacks.
3. **Meaningful Containers**:
   - Group nodes into clear boundaries: e.g. `Clients`, `Application / Plugin`, `Data Store`, `External Providers`.
   - Avoid deeply nested containers (> 2-3 levels) unless representing strict network/subscription boundaries.
4. **Edge Hygiene**:
   - Label every non-obvious arrow with *what* crosses it (e.g. `HTTPS / REST`, `Async Webhook`, `SQL`, `WP-Cron`).
   - Prefer orthogonal routing (`elk` in D2) over curved spaghetti lines.
5. **Contrast & Palette**:
   - Use restrained, high-contrast fills and borders so text is legible on both light and dark Markdown viewers.
   - Set an explicit light/neutral canvas background when embedding `.svg` in GitHub READMEs that may be viewed in dark mode.
