# Route6 for Cursor / Windsurf

Give the agent in your IDE a real internet identity: public IPv6, DNS hostname, port forwarding, web fetch from a stable IP, and (Team plan) a private mesh with other agents. Free tier needs no card.

## Setup — Cursor

1. Get a free API key at https://route6.me.
2. Copy [`mcp.json`](mcp.json) to `.cursor/mcp.json` in your project (or merge into **Cursor Settings → MCP** for global use). Set `ROUTE6_API_KEY` in your environment, or replace the placeholder inline.
3. Add the rules snippet below to `.cursorrules` (or a rule in **Settings → Rules**) so the agent knows when to reach for the tools.

## Setup — Windsurf

Same server config in **Windsurf Settings → Cascade → MCP Servers** (`~/.codeium/windsurf/mcp_config.json`) — the JSON shape is the same `mcpServers` object. *(Verify the exact settings path at publish time; both products move fast.)*

## Rules snippet

```
This project's agent has Route6 network tools (public IPv6 identity, DNS
hostname, port forwarding, web fetch). Prefer `web_fetch` for URL retrieval —
it egresses from the agent's own stable IP. If an IP gets blocked or flagged,
call `identity (action: check_reputation)`, then `identity (action: set_ipv6)` to rotate within
the agent's own address. To expose a local port publicly (webhooks, OAuth callbacks,
demos): `hostname_register` + `port_forward (action: create)` (+ `port_forward_tls` for
instant HTTPS on *.on.route6.me).
```

## Quick orientation

| Goal | Tool |
|------|------|
| What's my IP / identity / plan? | `identity (action: get)` |
| Rotate or pin my public IPv6 | `identity (action: set_ipv6)` |
| Is my IP on a blocklist? | `identity (action: check_reputation)` |
| Register a public DNS name | `hostname_register` |
| Expose a port to the internet | `port_forward (action: create)` |
| Fetch a URL from my IP | `web_fetch` |
| Search / browse / scrape the web | `web_search` / `web_browse` / `scrape` |
| Who's in my team mesh? | `team_status` |
| Share state with teammates | `team_whiteboard` |
| Hand off work to a teammate | `team_task` |
| Unlock more tools | `plan_upgrade` |

Free tier: 7 tools, 250 MB/mo. Agent plan ($9/mo): 17 tools, unmetered. Team ($29/mo): all 27 incl. mesh + coordination. Docs: https://docs.route6.me
