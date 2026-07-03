# Route6 Examples

**Give your AI agent its own internet identity** — a real public IPv6, a DNS hostname, inbound tunnels, and a private network to reach other agents. Controlled by the agent itself through 27 MCP tools. Free tier, no card.

Route6 is an alternative to ngrok/tunneling hacks and shared proxy pools, built for autonomous agents: the IP and hostname are *stable* (they survive restarts), the agent manages them itself over MCP, and every agent gets a dedicated `/64` from Route6's own address space.

- Website: https://route6.me · Docs: https://docs.route6.me
- Lite client: [`npm i -g @route6/agent`](https://www.npmjs.com/package/@route6/agent) · [`pip install route6`](https://pypi.org/project/route6/)
- Pro container: `route6me/netid` ([Docker Hub](https://hub.docker.com/r/route6me/netid))

## Quick start (lite — 3 commands, works behind any firewall/NAT)

```bash
npm install -g @route6/agent
route6 login sk_a6_...            # free key from https://route6.me
route6 tunnel start --hostname my-agent --to 8080
# → https://my-agent.on.route6.me now reaches localhost:8080
# → MCP proxy live at http://127.0.0.1:3000/mcp (all 27 tools for your editor/agent)
```

## Quick start (Pro — Docker, full WireGuard tunnel, routed /64 on the container)

See [`docker/`](docker/) — `docker compose up` with your API key in `.env`.

## Examples

| Example | What it shows | Plan |
|---------|---------------|------|
| [01 — Public webhook URL](examples/01-public-webhook-url/) | Stable public HTTPS endpoint for webhooks / OAuth callbacks (the ngrok use-case, minus the ephemerality) | Free key + lite, or Agent |
| [02 — Clean per-agent IP](examples/02-clean-ip-web-fetch/) | Fetch from your agent's own IP; check reputation; rotate inside your /64 when blocked | Free |
| [03 — Agent team coordination](examples/03-agent-team-coordination/) | Two agents share state (whiteboard), advertise capabilities, and hand off work (task queue) | Team |
| [04 — Agent-hosted service](examples/04-agent-hosted-service/) | An agent serves an API other agents reach by name | Agent |

## Editor / agent client configs

Config snippets to wire Route6's MCP tools into your coding agent: [Cursor / Windsurf](clients/cursor/) · [Cline](clients/cline/) · [Continue](clients/continue/) · [Hermes](clients/hermes/) · [Aider](clients/aider/) — plus the full [27-tool parameter reference](clients/hermes/references/tools.md).

Claude Code (one command):

```bash
claude mcp add --transport http route6 https://gw.route6.me/mcp \
  --header "Authorization: Bearer $ROUTE6_API_KEY"
```

## Tiers, honestly

- **Free:** 7 tools (identity, rotation, reputation check, ping/traceroute/DNS, basic `web_fetch`), 250 MB/mo.
- **Agent $9/mo:** 17 tools (adds hostname, port forwarding + TLS, search/browse/scrape, SMTP allowlist), unmetered bandwidth.
- **Team $29/mo:** all 27 (adds the private mesh + coordination: chat, whiteboard, capabilities, task queue, project tasks, roles).
- IPv6-only inside; IPv4 destinations work transparently via DNS64/NAT64. Outbound SMTP is blocked by default (allowlist up to 3 destinations). Sessions/bandwidth are logged; content is not inspected.

## License

Examples are [MIT](LICENSE). The Route6 clients and container are proprietary (freely installable, not open source).
