---
name: hermes-kanban-operations
description: "Use when operating Hermes Kanban multi-agent boards safely."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, kanban, dispatcher, multi-agent, profiles, reliability]
---

# Hermes Kanban Operations

## Purpose

Operate a Hermes Kanban board as a durable multi-agent work queue without turning a configuration error into a batch crash loop. This skill covers profile readiness, model/provider routing, dispatcher ownership, one-worker canaries, failure recovery, and artifact verification.

## Operating invariants

- A worker process starting is not success. Success requires a clean Kanban outcome and a verified deliverable.
- Never fan out a board before one canary task completes end to end.
- The task card is the effective execution contract. Pin `model` and `provider` on the canary/task when model routing matters; do not rely only on profile defaults.
- Use exactly one dispatcher. If `kanban.dispatch_in_gateway: true`, the gateway owns dispatch. Do not launch the deprecated standalone daemon alongside it.
- Treat provider quota/auth errors, no-TTY exits, missing profile configuration, and dead PIDs as different root-cause classes; inspect the worker log before retrying.
- Keep sibling tasks blocked until the canary is verified.
- For sensitive workflows, task instructions must prohibit spending, publishing, messaging, and irreversible changes unless a separately verified approval gate authorizes them.

## Profile readiness gate

For every assigned profile, verify:

1. `SOUL.md` exists and defines role, scope, output contract, and safety limits.
2. Resolved configuration contains a usable `model.default` and `model.provider`.
3. The selected provider is authenticated for that profile or its supported credential store.
4. Required skills/toolsets are available to the worker; avoid copying unnecessary skill trees or secrets into every profile.
5. The profile has a clear workspace and can write its expected artifact path.

Use the profile-scoped CLI (`hermes -p <profile> ...`) when checking values. Never print secret-bearing `.env` or auth files.

## Safe dispatch sequence

1. Create the board and verify it is the active board.
2. Create profiles and role instructions.
3. Create tasks with explicit assignees, bounded runtime, low retry count, and artifact requirements.
4. Keep all tasks blocked except one canary.
5. Set the canary's model/provider override explicitly with `hermes kanban set-model <task> <model> --provider <provider>` or task creation flags.
6. Unblock exactly one canary and dispatch with `--max 1 --failure-limit 1`.
7. Inspect `hermes kanban runs <task> --json`, `hermes kanban log <task>`, and `hermes kanban stats`.
8. Verify the artifact exists, is non-empty, and contains evidence appropriate to the task.
9. Only then unblock and dispatch the remaining tasks, using a controlled concurrency cap.

A reusable canary checklist and command pattern is in `references/hermes-kanban-canary.md`.

## Failure handling

- `pid not alive`: inspect the latest run and log; do not immediately increase retries or dispatch the batch.
- Provider error/429/auth failure: pin a known-good model/provider on the task, verify credentials, and retry one canary only.
- TUI/no-TTY/protocol violation: force the worker's CLI/non-interactive path and inspect profile interface settings.
- Missing artifact: the worker may have exited cleanly without satisfying the task. Reopen or request changes; do not mark success based on PID or exit code alone.
- Deprecated standalone daemon warning: stop the standalone process and use the gateway-embedded dispatcher, or explicitly choose a standalone deployment only when no gateway owns the board.

## Verification standard

Report separately:

- Board state: counts by status and assignee.
- Worker state: latest run outcome, error, duration, and provider/model evidence.
- Artifact state: absolute path, existence, byte size, line count, and a short content check.
- Safety state: what was explicitly not executed and what still requires approval.

Do not claim a task is running or complete from a dispatch response alone; re-read the board and artifact after the worker exits.
