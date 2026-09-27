---
name: hermes-custom-providers
description: "Add custom OpenAI-compatible LLM providers to Hermes Agent."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, providers, custom, openai-compatible, configuration]
    related_skills: [hermes-agent]
---

# Custom LLM Providers in Hermes Agent

Configure any OpenAI-compatible API endpoint as a **named custom provider** so you can switch to it with `/model custom:<name>:<model>` and persist it across sessions.

## When to Use

- You have an API key for a third-party gateway (APInex, Together AI, Groq, Perplexity, OpenRouter, etc.)
- You run a local inference server (Ollama, vLLM, llama.cpp, LM Studio)
- You want to use a corporate proxy or internal gateway
- You need multiple custom endpoints simultaneously

## Quick Setup (Interactive)

```bash
hermes model
# Select "Custom endpoint (self-hosted / VLLM / etc.)"
# Enter: API base URL, API key, Model name
```

This saves to `config.yaml` under `providers:` — the durable, multi-endpoint format.

## Manual Config (config.yaml)

```yaml
# ~/.hermes/config.yaml
providers:
  apinex:
    api: https://api.apinex.bond/v1
    key_env: APINEX_API_KEY
    transport: chat_completions
    default_model: free/mimo-v2.5

model:
  provider: custom:apinex
  default: free/mimo-v2.5
```

Then add the key to `~/.hermes/.env`:
```bash
echo "APINEX_API_KEY=sk-apx..." >> ~/.hermes/.env
```

## Switching at Runtime

```text
/model custom:apinex:free/gpt-5.6-luna
/model custom:apinex
/model custom:local:qwen2.5-coder:32b
```

## Common Providers — Ready Recipes

### APInex (free tier)
```yaml
providers:
  apinex:
    api: https://api.apinex.bond/v1
    key_env: APINEX_API_KEY
    transport: chat_completions
    default_model: free/mimo-v2.5
```
Free models: `free/mimo-v2.5`, `free/gpt-5.6-luna`, `free/glm-5.3-flash` — work with $0 balance.

### Together AI
```yaml
providers:
  together:
    api: https://api.together.xyz/v1
    key_env: TOGETHER_API_KEY
    transport: chat_completions
    catalog_provider: together
```

### Groq
```yaml
providers:
  groq:
    api: https://api.groq.com/openai/v1
    key_env: GROQ_API_KEY
    transport: chat_completions
```

### Local Ollama
```yaml
providers:
  local:
    api: http://localhost:11434/v1
    transport: chat_completions
```
⚠️ Set `OLLAMA_CONTEXT_LENGTH=64000` on the server — Hermes needs ≥64k context.

## Pitfalls & Gotchas

| Symptom | Cause | Fix |
|---------|-------|-----|
| `Unknown provider: apinex` | Used bare name instead of `custom:apinex` | Set `model.provider: custom:apinex` |
| HTTP 402 Insufficient balance | Paid model on free-tier key | Use `free/*` models or add USD balance |
| Timeout on first request | Cold start / slow upstream | Increase `model.timeout` or retry |
| `/models` returns 404 | Endpoint doesn't expose catalog | Set `default_model` and `discover_models: false` |
| Vision not working | Model supports vision but Hermes doesn't know | Add `supports_vision: true` |
| Key goes stale mid-session | Short-lived bearer from SSO/IAM | Use `key_cmd: "my-auth-cli print-token --profile prod"` |

## Verification

```bash
curl -s https://api.apinex.bond/v1/chat/completions \
  -H "Authorization: Bearer $APINEX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"free/mimo-v2.5","messages":[{"role":"user","content":"OK"}]}'

hermes chat -q "OK" --provider custom:apinex --model free/mimo-v2.5
```

## References

- `references/apinex.md` — APInex-specific details (models, pricing, auth)
- `references/together-ai.md` — Together AI recipe
- `references/groq.md` — Groq recipe
- `references/ollama.md` — Ollama local setup with context length fix