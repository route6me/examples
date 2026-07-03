# Route6 for Continue

Route6 gives your agent a real internet identity — public IPv6, DNS hostname, port forwarding, web fetch from a stable IP. Free tier needs no card: get a key at https://route6.me.

## Setup

Add to your Continue config (`~/.continue/config.yaml`, or an `mcpServers` block in a workspace assistant):

```yaml
mcpServers:
  - name: route6
    type: streamable-http
    url: https://gw.route6.me/mcp
    requestOptions:
      headers:
        Authorization: "Bearer ${{ secrets.ROUTE6_API_KEY }}"
```

*(Schema per Continue's MCP docs as of mid-2026 — verify field names at publish time.)*

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
