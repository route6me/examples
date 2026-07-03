# Route6 skill — Hermes render

Package for the **Hermes Skills Hub** (`hermes skills install route6/route6` once published). Hermes is a native MCP client, so Route6 works with zero plugin code — this package is the SKILL.md (agentskills.io format, identical body to the Claude Code render) plus the connection wiring.

## Install (manual, works today)

1. Get a free API key at https://route6.me (no card).
2. Add to `~/.hermes/config.yaml`:

```yaml
mcp_servers:
  route6:
    url: "https://gw.route6.me/mcp"
    headers:
      Authorization: "Bearer <ROUTE6_API_KEY>"
    timeout: 180
```

3. Restart Hermes — all 27 Route6 tools are discovered at startup.

## Render rule

Do **not** edit `SKILL.md` here — it is generated from the shared Route6 skill source (`render.py` in the route6-skills render set) so all client renders stay identical. `references/tools.md` is generated from the `@route6/mcp-core` tool schemas.
