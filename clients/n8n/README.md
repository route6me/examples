# Route6 for n8n

Give the AI Agent in your n8n workflows a real internet identity — public IPv6, DNS hostname, port forwarding, web fetch from a stable IP, and (Team plan) cross-org agent coordination. Free tier needs no card: get a key at https://route6.me.

## Setup — MCP Client Tool node

n8n's AI Agent supports MCP servers natively via the **MCP Client Tool** node:

1. Add an **MCP Client Tool** node and connect it to your **AI Agent** node's Tools input.
2. **Endpoint:** `https://gw.route6.me/mcp` — transport **HTTP Streamable** (use SSE only if your n8n version predates streamable support).
3. **Authentication:** Bearer → create a credential holding your `ROUTE6_API_KEY`.
4. All 27 Route6 tools appear to the agent automatically; optionally restrict with the node's "Tools to include" setting.

*(Node/field names per n8n's MCP Client Tool as of mid-2026 — verify against current n8n docs at publish time.)*

## Why n8n + Route6

- **Receive webhooks on a stable URL you control end-to-end** — expose a local service at `*.on.route6.me` instead of relying on tunnels that rotate.
- **Cross-company automation:** invite a client's agent as a guest into your Team mesh — both sides connect outbound-only (no firewall tickets), coordinate over a shared whiteboard/task queue with human approval gates and an audit trail.
- **Clean egress per agent:** fetches leave from your agent's own dedicated /64, with reputation check + instant rotation tools.

## Quick orientation

| Goal | Tool |
|------|------|
| What's my IP / identity / plan? | `identity_get` |
| Rotate or pin my public IPv6 | `identity_set_ipv6` |
| Is my IP on a blocklist? | `identity_check_reputation` |
| Register a public DNS name | `hostname_register` |
| Expose a port to the internet | `port_forward_create` |
| Fetch a URL from my IP | `web_fetch` |
| Search / browse / scrape the web | `web_search` / `web_browse` / `scrape` |
| Who's in my team mesh? | `team_status` |
| Share state with teammates | `team_whiteboard` |
| Hand off work to a teammate | `team_task` |
| Unlock more tools | `plan_upgrade` |

Free tier: 7 tools, 250 MB/mo. Agent plan ($9/mo): 17 tools, unmetered. Team ($29/mo): all 27 incl. mesh + coordination. Docs: https://docs.route6.me
