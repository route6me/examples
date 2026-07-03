# 04 — Your agent hosts a service other agents reach by name (Agent plan)

**Problem:** the emerging agent-to-agent pattern needs agents to *expose* stable, discoverable endpoints — an API, an MCP server, a status page — which is impossible on ephemeral IPs and NAT'd machines.

**With Route6** the agent gets a name and makes itself reachable at it. The name and IP survive restarts, so other agents can hard-code it.

## Serve

```bash
# something to serve — say a tiny status API on localhost:9000
python3 -m http.server 9000 &

# lite path: one command
route6 tunnel start --hostname data-agent --to 9000
```

or agent-driven on the Pro container:

```jsonc
hostname_register   { "name": "data-agent" }
port_forward_create { "external_port": 443, "internal_port": 9000, "protocol": "tcp" }
port_forward_tls    { "port": 443, "action": "enable" }
```

## Consume (from any other agent, any plan — plain HTTPS)

```jsonc
web_fetch { "url": "https://data-agent.on.route6.me/status.json" }
```

The consuming agent needs no special setup — `*.on.route6.me` is public DNS with valid TLS. If both agents are on the same Team, they can additionally reach each other over the private mesh (see [example 03](../03-agent-team-coordination/)) without touching the public internet at all.

**Composability note:** the served endpoint can itself be an MCP server — an agent exposing tools to other agents at a stable public URL is exactly this recipe.
