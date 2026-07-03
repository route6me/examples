# 01 — A stable public HTTPS URL for your agent (webhooks, OAuth callbacks)

**Problem:** your agent runs on a laptop / VM behind NAT and needs to *receive* something — a Stripe/GitHub webhook, an OAuth redirect, a callback. ngrok-style tunnels work but the URL changes on restart and isn't agent-controlled.

**With Route6 the URL is stable** (`my-agent.on.route6.me` survives restarts) and the agent can manage it itself.

## Path A — lite client (no Docker, outbound HTTPS only)

```bash
# terminal 1: the thing that should receive the webhook
python3 webhook_server.py            # listens on localhost:8080

# terminal 2: expose it
route6 login sk_a6_...               # once
route6 tunnel start --hostname my-agent --to 8080
```

Give out `https://my-agent.on.route6.me/hook` as your webhook URL. Test:

```bash
curl -X POST https://my-agent.on.route6.me/hook -d '{"event":"ping"}'
```

## Path B — Pro container, agent-driven via MCP (Agent plan)

The agent itself calls (tool → arguments):

```jsonc
hostname_register     { "name": "my-agent" }
// → my-agent.on.route6.me (AAAA + PTR), propagates ≤60 s

port_forward_create   { "external_port": 8443, "internal_port": 8080,
                        "protocol": "tcp", "ttl_seconds": 3600 }
// ttl_seconds is optional — great for one-shot OAuth callbacks: it auto-expires

port_forward_tls      { "port": 8443, "action": "enable" }
// Route6 terminates TLS with the *.on.route6.me wildcard cert → instant valid HTTPS
```

Webhook URL: `https://my-agent.on.route6.me:8443/hook`. Cleanup is `port_forward_delete { "external_port": 8443 }` — or let the TTL do it.

`webhook_server.py` in this directory is a dependency-free receiver you can use for either path.
