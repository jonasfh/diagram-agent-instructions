# diagram-agent-instructions

General AI agent instructions, skills, and self-bootstrapping rendering scripts for producing professional architecture, workflow, and infrastructure diagrams using **Mermaid**, **D2**, and **Python `diagrams` (`mingrammer/diagrams`)**.

## Tooling Philosophy

- **SVG-first**: Always output `.svg` by default (use `.png` only when raster is clearly advantageous or a specific viewer/embed target has poor SVG support).
- **Right tool for the job**:
  - **Mermaid**: Simple inline Markdown diagrams (`README.md`, `DEV_README.md`, PRs), small sequence diagrams (< 10 nodes), and `erDiagram`.
  - **D2 (CLI + `--layout=elk`)**: Complex system architectures, layered components, integration flows, and workflows with custom or vendor SVG icons.
  - **Python `diagrams`**: Cloud and infrastructure topologies (especially **Azure**, Kubernetes, VNet/hybrid) where official cloud provider icons and `Cluster` boundaries shine.
- **Self-bootstrapping**: Rendering scripts automatically install `d2` (static binary) and Python `diagrams` (isolated venv) into `~/.cache/diagram-agent-tools/` on first run—no project `Dockerfile` edits required.

---

## Installation

### Option 1: Git Submodule + Antigravity `skills.json` (Zero Symlinks)

Add as a submodule in `.agents/diagram-agent-instructions`:

```bash
git submodule add https://github.com/jonasfh/diagram-agent-instructions.git .agents/diagram-agent-instructions
```

Create `.agents/skills.json` so Antigravity discovers all skills automatically without symlinks:

```json
{
  "entries": [
    { "path": "diagram-agent-instructions/skills" }
  ]
}
```

Reference `DIAGRAM_GUIDELINES.md` in your project's `AGENTS.md`:

```markdown
- 📊 **[Diagram Guidelines](file:///.agents/diagram-agent-instructions/DIAGRAM_GUIDELINES.md)**: Tool selection (Mermaid vs. D2 vs. Python diagrams), SVG-first policy, vendor icons, and visual verification.
```

### Option 2: Cross-Agent CLI (`npx skills`)

Compatible with Antigravity, Claude Code, Cursor, GitHub Copilot, and Codex:

```bash
npx skills add jonasfh/diagram-agent-instructions
```

---

## Optional: Bake Tools into a `Dockerfile`

The included `ensure_tools.py` scripts work out of the box without modifying your container image. If your team prefers pre-installed tools for offline use or faster CI, add this snippet to your `Dockerfile`:

```dockerfile
# Graphviz (required by Python diagrams)
RUN apt-get update && apt-get install -y --no-install-recommends graphviz \
    && rm -rf /var/lib/apt/lists/*

# D2 CLI
RUN curl -fsSL https://d2lang.com/install.sh | sh -s --

# Python diagrams in an isolated venv
RUN python3 -m venv /opt/diagrams-venv \
    && /opt/diagrams-venv/bin/pip install --no-cache-dir diagrams
ENV PATH="/opt/diagrams-venv/bin:$PATH"
```

## License

[CC0 1.0 Universal](LICENSE)
