---
name: telegram-approval-workflows
description: "Use for Telegram approval buttons and callback execution."
version: 1.0.0
license: MIT
---

# Telegram Approval Workflows

Use this skill when a Telegram bot must present an approval decision and reliably turn a user's tap into a recorded, authorized outcome.

## Core rule

A Telegram inline keyboard is only presentation. A button is functional only when all of these exist:

1. The message is sent by the same bot instance that owns the update consumer.
2. `callback_data` uses a callback namespace that the consumer actually handles.
3. The consumer has registered pending state for the specific prompt/action.
4. The clicker's Telegram user ID is authorized.
5. The callback is acknowledged with `answerCallbackQuery` / the framework equivalent.
6. The message is edited or a follow-up message confirms the recorded decision.
7. For real actions, the current action payload is re-read and compared with the version shown to the user before execution.

Never call a message with visible buttons a working approval until a real click has produced an observable confirmation.

## Safe implementation sequence

1. Send a no-side-effect test prompt with three choices: approve, defer, reject.
2. Click each button from the authorized Telegram account.
3. Verify both the Telegram response and the gateway log/event record.
4. Add a correlation ID, action version/hash, expiry, and actor ID to production prompts.
5. On click, revalidate live state (price, stock, budget, target, permissions, and current action version).
6. If anything changed, reject execution and ask for a fresh approval.
7. Execute only the exact approved action; never treat approval as a blanket permission.
8. Persist the decision and reason for rejections.

## Hermes-specific guidance

Hermes Telegram handlers are stateful. In Hermes v0.20.1, the adapter registers a `CallbackQueryHandler`, but the handler routes only known namespaces such as `cl:` (clarify), `sc:` (slash confirmation), `ea:` (exec approval), model-picker prefixes, and other built-in prefixes. Arbitrary callback data sent directly through the Bot API is not automatically routed to a handler.

For a real Hermes workflow, prefer the native stateful prompt mechanism (`clarify` or the relevant built-in confirmation primitive) rather than sending raw Telegram buttons from a shell script. If a custom approval domain is required, implement it as a maintained adapter/plugin extension with explicit authorization, state registration, expiry, and tests. Do not claim success from `sendMessage` returning `ok: true`; that verifies delivery only, not callback handling.

## User-facing format

For a non-technical owner, put the decision and money first. Keep the message short:

```text
🟡 APROBACIÓN — [AGENTE]

Qué: [acción exacta]
Plata en juego: $[monto]
Producto/destino: [live value]
Riesgo: [one line]

[ ✅ PRENDER ] [ ⏸ DESPUÉS ] [ ❌ NO ]
```

After a tap, show a confirmation such as `Registré: PRENDER ✅` and remove or disable the buttons. If the state changed, show `No ejecuté: cambió [dato]. Necesita una aprobación nueva.`

## Testing checklist

- [ ] Bot receives ordinary text.
- [ ] Authorized user ID is allowlisted.
- [ ] Test message contains the intended callback namespace.
- [ ] Callback update is observed in gateway logs.
- [ ] Telegram spinner stops / callback is answered.
- [ ] Confirmation appears in the chat.
- [ ] Buttons are removed or made idempotent.
- [ ] Duplicate taps do not execute twice.
- [ ] Expired prompts are rejected.
- [ ] Unauthorized taps are rejected.
- [ ] A changed price, stock, budget, or target forces re-approval.
- [ ] No production agent is connected before the no-side-effect test passes.

## Pitfalls

- Treating a successful outbound API response as proof of an interactive circuit.
- Using arbitrary callback strings with no handler.
- Registering a handler but not registering matching pending state.
- Forgetting to acknowledge the callback, leaving Telegram's spinner active.
- Executing from stale prompt text instead of re-reading live state.
- Testing only the green button; test defer and reject too.
- Patching a bundled Hermes installation without a restart and then assuming the running gateway has the patch.

## Reference

See `references/hermes-telegram-callbacks.md` for the verified Hermes v0.20.1 routing map and a reproducible, no-side-effect diagnostic checklist.
