# Route6 for Aider

**Honest status:** Aider has no native MCP client support (as of mid-2026 — re-verify at publish time). Route6's tools therefore can't be wired into Aider directly the way they are in Cursor/Cline/Continue.

Working options today:

1. **MCP-to-CLI bridge** — run a community MCP bridge (e.g. `mcpm`/`mcp-proxy`-style tools) that exposes MCP servers as shell commands, and let Aider call them via its run-command flow. Point the bridge at `https://gw.route6.me/mcp` with `Authorization: Bearer <ROUTE6_API_KEY>`.
2. **Lite client CLI** — `pip install route6` installs the Route6 thin client; the agent (or you) can call the gateway directly over HTTPS from scripts Aider writes.

If/when Aider ships MCP support, the config will be the same URL + Bearer wiring as every other client here — no Route6-side changes needed.

Free tier: 7 tools, 250 MB/mo, no card — key at https://route6.me. Docs: https://docs.route6.me
