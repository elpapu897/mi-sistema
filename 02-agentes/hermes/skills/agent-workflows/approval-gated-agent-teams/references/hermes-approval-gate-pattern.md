# Hermes approval-gate pattern

## State machine

```text
pending
  ├─ postpone → postponed
  ├─ reject   → rejected
  ├─ expiry   → expired
  └─ approve → approved_pending_revalidation
                         ├─ snapshot mismatch → blocked_changed
                         └─ identical → ready_to_execute → executor result
```

## Minimal persisted record

```json
{
  "id": "approval-123",
  "kind": "campaign_enable",
  "title": "Prender campaña X",
  "snapshot": {
    "campaign_id": "…",
    "budget_ars_day": 1500,
    "destination": "…",
    "product_id": "…",
    "price_ars": 16990,
    "stock": 12,
    "payload_version": 1
  },
  "snapshot_hash": "sha256(canonical(snapshot))",
  "status": "pending",
  "created_at": "…",
  "expires_at": "…",
  "resolved_by": null
}
```

Canonicalize JSON with sorted keys and stable separators before hashing. Never hash only the message text: mutable business facts belong in the snapshot.

## Callback contract

The Telegram callback should:

1. Authenticate the caller and chat.
2. Parse and validate the approval ID and allowed action.
3. Persist the state transition.
4. Answer the callback so the client stops showing a spinner.
5. Remove or replace the buttons so the same request cannot be clicked repeatedly.
6. Never call Shopify, Meta, email, WhatsApp, or publishing APIs.

## Revalidation contract

The executor must fetch live state and compare the canonical snapshot. At minimum compare every value that can change the business outcome: price, stock, shipping, budget, audience/destination, campaign status, theme version, message recipient, and content hash. Any mismatch invalidates the approval and requires a new request.

## Rollout test

Before enabling real side effects, create a harmless request with zero budget and no external target. Verify:

- click approval → `approved_pending_revalidation`;
- identical payload → `ready_to_execute`;
- changed payload → `blocked_changed`;
- second click or stale request cannot execute.

## Hermes-specific lesson

A profile can be created as a lightweight worker with a role-specific `SOUL.md`; do not confuse that with a running agent. Schedule/dispatch only after the profile, task, skill/model selection, output path, verifier, and side-effect gate are defined. Keep the approval broker in the gateway rather than making SEMÁFORO another worker persona.
