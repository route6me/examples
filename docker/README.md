# Route6 Pro — Docker install

The Pro tier runs the `route6me/netid` container on **your** machine: it brings up a WireGuard tunnel and puts a real, routed public IPv6 (from your dedicated /64) on the container's network stack. Any process inside egresses from your agent's own IP; the MCP server is available to the host at `http://127.0.0.1:3000/mcp`.

```bash
cp .env.example .env       # put your API key in
docker compose up -d
curl -s http://127.0.0.1:3000/mcp   # MCP endpoint (streamable HTTP)
```

Notes:

- `cap_add: NET_ADMIN` is required (WireGuard + firewall rules inside the container). Without it, parts of the setup fail silently.
- The MCP port is deliberately mapped to `127.0.0.1` only, and the container firewalls port 3000 on its public IPv6 — the MCP server is never internet-reachable.
- One live connection per agent: starting a second container with the same key disconnects the first.
- If you don't want Docker, the lite client (`npm i -g @route6/agent`) covers most use-cases over outbound HTTPS only — see the repo README.
