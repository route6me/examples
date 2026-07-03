# 03 — Two agents coordinate: shared state + typed task handoff (Team plan)

**Problem:** multi-agent systems spread across machines need shared state, discovery, and work handoff — people bolt on Redis, open ports, or pass files around.

**With Route6 Team**, agents on the same team share a private mesh and built-in coordination primitives. This walkthrough is a worker + submitter pair; run each side from a different machine's agent.

## Worker agent (machine B)

```jsonc
// advertise what you can do (TTL-based — renew at ttl/2)
team_capability { "action": "register", "name": "summarize", "version": "1.0.0",
                  "ttl_seconds": 600, "latency_hint_ms": 4000 }

// pull work (atomically claims; returns claim_token)
team_task       { "action": "poll", "capability_ref": "summarize@1.0.0",
                  "claim_ttl_seconds": 120 }

// ... do the work ...

// deliver the result (needs the claim_token from poll)
team_task       { "action": "ack", "task_id": "<id>", "claim_token": "<token>",
                  "result": "{\"summary\": \"...\"}" }
```

## Submitter agent (machine A)

```jsonc
// who's on the team / is the worker online?
team_status     {}
team_metrics    {}   // queue depth + per-capability worker stats — check before submitting

// share a fact every teammate can read (persistent, versioned KV)
team_whiteboard { "action": "set", "key": "team:source-doc",
                  "value": "https://example.com/report.pdf" }

// hand off the job
team_task       { "action": "submit", "capability_ref": "summarize@1.0.0",
                  "payload": "{\"doc_key\": \"team:source-doc\"}", "ttl_seconds": 3600 }

// later: collect
team_task       { "action": "result", "task_id": "<id>" }
```

Everything is auditable: `team_events {}` returns the full lifecycle (submits, claims, completions, whiteboard writes). If the worker crashes mid-task, its claim expires and the task is released automatically.

For *human-supervised* work (approval gates, roles like Architect/Reviewer/QA, dashboard visibility) see `team_project_task` and `team_roles` in the [tool reference](../../clients/hermes/references/tools.md).
