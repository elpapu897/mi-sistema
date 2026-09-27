# Together AI Provider Reference

## Base URL
```
https://api.together.xyz/v1
```

## Authentication
```
Authorization: Bearer $TOGETHER_API_KEY
Content-Type: application/json
```

## Config
```yaml
providers:
  together:
    api: https://api.together.xyz/v1
    key_env: TOGETHER_API_KEY
    transport: chat_completions
    catalog_provider: together  # inherits model metadata from Hermes catalog
```

## Popular Models
- `meta-llama/Llama-3.3-70B-Instruct-Turbo`
- `meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo`
- `Qwen/Qwen2.5-72B-Instruct-Turbo`
- `deepseek-ai/DeepSeek-V3`
- `google/gemma-2-27b-it`

## Notes
- Significantly cheaper than first-party APIs
- Good default for multi-model fleets
- Get key at: https://api.together.xyz/settings/api-keys