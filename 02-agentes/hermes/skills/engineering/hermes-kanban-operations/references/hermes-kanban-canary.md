# Hermes Kanban Canary Runbook

Use this runbook before dispatching a batch.

## Readiness commands

```bash
hermes kanban boards current
hermes -p <profile> config get model.default
hermes -p <profile> config get model.provider
hermes -p <profile> auth status <provider>
hermes config get kanban.dispatch_in_gateway
hermes gateway status
```

Never read or print `.env` or auth files; they may contain credentials.

## One-worker canary

Create sibling tasks as `blocked`, then unblock only one. Pin the task:

```bash
hermes kanban set-model <task_id> <model> --provider <provider>
hermes kanban unblock <task_id>
hermes kanban dispatch --max 1 --failure-limit 1 --json
```

## Verification loop

```bash
hermes kanban list --status running --json
hermes kanban runs <task_id> --json
hermes kanban log <task_id> --tail 10000
hermes kanban stats
```

Do not call the canary successful until its latest run is `outcome=completed`, the task is `done` or `review`, and its artifact is verified with a file existence/size/content check.

## Failure matrix

- `pid not alive`: inspect the latest worker log and process/run record before retrying.
- Provider `401`, `429`, or quota error: verify auth and pin model/provider on the card; retry one canary only.
- TUI/no-TTY/protocol violation: use the worker CLI/non-interactive path and inspect profile interface settings.
- No artifact: treat as incomplete even if the process exited with code 0.
- `hermes kanban daemon` says deprecated: use the gateway-embedded dispatcher when `kanban.dispatch_in_gateway=true`; never run both dispatchers.

Only after a clean canary should siblings be unblocked and dispatched with a controlled concurrency cap.