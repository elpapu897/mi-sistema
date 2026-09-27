# APInex Provider Reference

## Base URL
```
https://api.apinex.bond/v1
```

## Authentication
```
Authorization: Bearer sk-apx_...
Content-Type: application/json
```

## Models & Pricing (Live as of 2026-09-18)

| Model ID | Price / 1M tokens | Context | Notes |
|----------|-------------------|---------|-------|
| `free/mimo-v2.5` | FREE | 1M | ✅ Works with $0 balance |
| `free/gpt-5.6-luna` | FREE | 1M | ✅ Works with $0 balance |
| `free/glm-5.3-flash` | FREE | 1M | ✅ Works with $0 balance |
| `free/gemini-3.8-flash` | $0.75 (Sub) | 1M | ⚠️ Subscription only |
| `free/claude-sonnet-4.6` | $1.50 (Sub) | 1M | ⚠️ Subscription only |
| `free/claude-opus-4.6` | $1.50 (Sub) | 1M | ⚠️ Subscription only |
| `gpt-5.6-sol` | $0.25 | 1M | 💰 Paid — needs USD balance |
| `gpt-5.6-terra` | $0.17 | 1M | 💰 Paid |
| `gpt-5.6-luna` | $0.07 | 1M | 💰 Paid |
| `claude-fable-5.1` | $2.00 | 1M | 💰 Paid |
| `deepseek-v4.1-flash` | $0.06 | 1M | 💰 Paid |
| `gemini-3.8-flash` | $0.10 | 1M | 💰 Paid |
| `glm-5.3-flash` | $0.05 | 1M | 💰 Paid |

## Endpoints
- `POST /v1/chat/completions` — OpenAI-compatible chat
- `POST /v1/responses` — OpenAI Responses API
- `POST /v1/messages` — Anthropic Messages API
- `GET /v1/models` — List available models
- `GET /v1/balance` — Check USD balance

## Quick Test
```bash
curl -s https://api.apinex.bond/v1/chat/completions \
  -H "Authorization: Bearer $APINEX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"free/mimo-v2.5","messages":[{"role":"user","content":"test"}]}'
```

## Balance Check
```bash
curl -s https://api.apinex.bond/v1/balance \
  -H "Authorization: Bearer $APINEX_API_KEY"
```

## Notes
- Single USD wallet for all models + tools
- Free tier models have `weight` multiplier for internal billing (×1–×4)
- Free models work with $0 balance; paid models require top-up
- Get key at: https://apinex.bond/keys