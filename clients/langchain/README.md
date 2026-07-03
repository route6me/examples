# Route6 for LangChain / LangGraph

Give your LangChain or LangGraph agent a real internet identity — public IPv6, DNS hostname, port forwarding, web fetch from a stable IP, and (Team plan) a private mesh with other agents. Free tier needs no card: get a key at https://route6.me.

## Setup — `langchain-mcp-adapters`

```bash
pip install langchain-mcp-adapters
```

```python
import os
from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient({
    "route6": {
        "transport": "streamable_http",
        "url": "https://gw.route6.me/mcp",
        "headers": {"Authorization": f"Bearer {os.environ['ROUTE6_API_KEY']}"},
    }
})

tools = await client.get_tools()          # all 27 Route6 tools as LangChain tools

# use them in any agent, e.g. LangGraph:
from langgraph.prebuilt import create_react_agent
agent = create_react_agent("anthropic:claude-sonnet-5", tools)
```

*(API per `langchain-mcp-adapters` as of mid-2026 — verify the import path/signature against current docs at publish time.)*

## Typical patterns

- **Research agents with a clean identity:** `web_fetch` egresses from the agent's own /64; on a block, `identity_check_reputation` → `identity_set_ipv6` rotates instantly.
- **Agents that receive callbacks:** `hostname_register` + `port_forward_create` (+ `port_forward_tls`) give the agent a stable public HTTPS endpoint for webhooks/OAuth.
- **Multi-agent LangGraph across machines (Team):** share facts via `team_whiteboard`, hand off typed work via `team_capability`/`team_task` with claim/ACK semantics — no Redis to bolt on.

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
