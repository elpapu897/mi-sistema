---
name: approval-gated-agent-workflows
description: "Use for approval-gated autonomous agent workflows."
version: 1.0.0
license: MIT
---

# Approval-Gated Agent Workflows

Use this skill when an autonomous agent system can spend money, publish publicly, contact customers, modify production systems, or otherwise create an external side effect that requires human approval.

## Core design

Separate four concerns:

1. **Proposal** — an agent prepares a bounded action and explains its business impact.
2. **Approval request** — a durable record freezes exactly what the human is being asked to approve.
3. **Decision callback** — the channel records the human's choice and acknowledges it visibly.
4. **Execution gate** — a separate executor rereads live state, revalidates the snapshot, and only then performs the side effect.

Never let a UI button directly call an unrestricted executor.

## Durable approval record

Persist at least:

- unique approval ID;
- action type and human-readable title/body;
- canonical snapshot JSON;
- snapshot hash;
- creator/agent;
- allowed user IDs;
- created and expiry timestamps;
- status;
- selected choice and approving user;
- execution result or block reason.

Use explicit states such as:

```text
pending
approved_pending_revalidation
ready_to_execute
postponed
rejected
expired
blocked_changed
executed
failed
```

Canonicalize JSON with stable key ordering before hashing. Make duplicate clicks idempotent: a resolved request must not execute or change state a second time.

## Callback-channel verification

A message being delivered with inline buttons proves only that the channel accepted the markup. It does **not** prove that callbacks are wired.

End-to-end verification must prove:

1. the callback data uses a format the adapter actually handles;
2. the clicking user is authorized at callback time;
3. the handler records the decision;
4. the channel acknowledges the click;
5. the message is edited or followed up with the recorded result;
6. duplicate/stale clicks are handled visibly.

For Hermes Telegram, prefer registered stateful primitives such as the built-in clarify/confirmation callback formats when they fit. If a domain workflow needs custom buttons, add a narrowly scoped handler plus a durable broker. Arbitrary `callback_data` is only visual until a registered handler consumes it.

## Snapshot revalidation

Approval must be bound to the exact state shown to the human. Immediately before execution:

1. reread every relevant live value;
2. build the same canonical snapshot shape;
3. recompute its hash;
4. compare it with the stored approval hash;
5. if any relevant value differs — price, stock, budget, campaign ID, destination, public text, or version — mark `blocked_changed` and request approval again;
6. execute only from `ready_to_execute` or an equivalent validated state.

An approval for a stale price, stale product, stale stock state, or changed budget is not approval for the new action.

## Safe rollout sequence

1. Implement and test the broker with a no-op action.
2. Test approve, postpone, reject, expiry, unauthorized user, duplicate click, identical snapshot, and changed snapshot.
3. Connect read-only/audit agents first.
4. Add one real executor at a time, each with its own whitelist and revalidation function.
5. Keep money/publication/message actions blocked until the corresponding executor has a verified test.
6. Log every decision and surface only urgent items plus the agreed daily summary to the human.

## Multi-agent integration

Use a durable queue or Kanban task board for proposals and handoffs. Agents may create work for one another, but side-effect tasks must terminate at the approval gate. The orchestrator should pass bounded artifacts and hashes rather than full upstream conversations.

For large research or planning tasks, use a fan-out/fan-in swarm:

```text
workers → verifier → synthesizer → approval gate (if side effect)
```

Use scheduled runs to wake agents when needed instead of keeping many long-running model conversations alive. Pin cheaper models for routine extraction/classification and reserve stronger models for verification and synthesis.

## Verification checklist

Before calling the workflow production-ready, verify with real tool output:

- broker database/file exists and survives restart;
- callback handler is loaded after gateway restart;
- Telegram click produces an acknowledgement and a state transition;
- identical snapshot passes revalidation;
- changed snapshot is blocked;
- expiry and duplicate click are idempotent;
- no money/publication/message executor is reachable from the test action;
- logs contain a redacted approval ID, choice, actor, and resulting status.

## Pitfalls

- Sending buttons through a raw Telegram API call and assuming Hermes will handle arbitrary callback IDs.
- Treating an HTTP `sendMessage` success response as callback success.
- Executing inside the callback handler before rereading live Shopify/Meta state.
- Storing only the human-readable message and not the structured snapshot.
- Allowing a stale approval to authorize a changed budget, product, price, stock, destination, or public text.
- Building all agents before testing the approval gate.
- Claiming a dashboard is a visual Kanban board without verifying that the installed dashboard exposes Kanban views.

See `references/hermes-telegram-callbacks.md` for the concrete debugging pattern and test matrix.
