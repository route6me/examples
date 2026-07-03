# 02 — Fetch from your agent's own clean IP (and rotate when blocked)

**Problem:** agents that fetch the web from shared proxy pools inherit the pool's reputation — blocklists, CAPTCHAs, bans. Residential proxies are expensive and opaque.

**With Route6** every agent has a dedicated public IPv6 /64 from Route6's own address space (own ASN, own abuse contact, forward-confirmed rDNS). Your agent fetches from *its* IP, checks *its* reputation, and rotates inside *its own* /64 — instantly, because the whole /64 is routed to the agent.

All four tools below are on the **free tier**.

```jsonc
// who am I?
identity_get              {}
// → active IPv6, the /64 prefix, hostname, plan

// fetch from my IP
web_fetch                 { "url": "https://api.ipify.org?format=json" }
// → shows YOUR agent IP as the source

// is my IP on a blocklist?
identity_check_reputation {}
// → DNSBL results for the active address

// listed somewhere, or just want a fresh address? rotate:
identity_set_ipv6         {}
// omit "address" → random unused address inside your /64, effective immediately

// verify the change
web_fetch                 { "url": "https://api.ipify.org?format=json" }
```

The hygiene loop an agent can run autonomously: `identity_check_reputation` → if listed → `identity_set_ipv6` → re-check.

**Honest notes:** these are datacenter-class IPs (Route6's own PI space) — sites that block by ASN class will still block them; rotation helps with per-IP blocks, not with that. IPv4-only destinations work transparently through DNS64/NAT64.
