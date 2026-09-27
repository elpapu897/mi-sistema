# Hermes v0.20.1 Telegram callback notes

## Verified routing

The installed Telegram adapter registers `CallbackQueryHandler(self._handle_callback_query)` and polls with `Update.ALL_TYPES`, so this version has native callback-query support.

The handler dispatches by callback-data namespace. Verified namespaces in the adapter include:

- `cl:` — stateful clarify choices; requires a live clarify entry.
- `sc:` — slash confirmation; requires a pending confirmation ID/state.
- `ea:` — execution approval; requires registered approval state and authorized user.
- model/choice picker namespaces — internal picker state.
- `update_prompt:` — update watcher prompt.

Unknown callback-data strings fall through without a user-facing response. Therefore, a Bot API `sendMessage` returning `ok: true` proves only that the message and keyboard were delivered.

## Reproduction recipe

1. Send a message with arbitrary callback data such as `gonvra_test_ok` through the Bot API.
2. Confirm Telegram displays the buttons.
3. Tap a button.
4. Inspect the gateway log: no domain handler will resolve it because the namespace is unknown.
5. Compare with a native Hermes prompt: it creates state first, sends a known namespace, validates the caller, acknowledges the query, and edits or follows up on the message.

## Safe next move

For production, use the native stateful prompt primitive where possible. If a GONVRA-specific approval domain is needed, add a maintained plugin/adapter extension rather than relying on raw Bot API buttons. The extension must include authorization, pending state, expiry, idempotency, live-state revalidation, callback acknowledgement, and end-to-end tests.

## Operational pitfall

A source patch to the installed Hermes gateway is not active until the gateway process is restarted. Verify the running process/version after restart before sending a new test.
