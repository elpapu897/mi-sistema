# Groq Provider Reference

## Base URL
```
https://api.groq.com/openai/v1
```

## Authentication
```
Authorization: Bearer $GROQ_API_KEY
Content-Type: application/json
```

## Config
```yaml
providers:
  groq:
    api: https://api.groq.com/openai/v1
    key_env: GROQ_API_KEY
    transport: chat_completions
```

## Popular Models (Free Tier Available)
- `llama-3.3-70b-versatile`
- `llama-3.1-8b-instant`
- `mixtral-8x7b-32768`
- `gemma2-9b-it`

## Notes
- Very fast inference (LPU hardware)
- Generous free tier
- Get key at: https://console.groq.com/keys