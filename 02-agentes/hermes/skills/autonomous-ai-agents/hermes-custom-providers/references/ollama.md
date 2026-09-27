# Ollama Local Provider Reference

## Base URL
```
http://localhost:11434/v1
```

## Authentication
None required for local Ollama.

## Config
```yaml
providers:
  local:
    api: http://localhost:11434/v1
    transport: chat_completions
```

## Critical: Context Length

**Ollama defaults to very low context lengths** — Hermes needs ≥64k.

| Available VRAM | Default Context |
|----------------|-----------------|
| < 24 GB        | 4,096 tokens    |
| 24–48 GB       | 32,768 tokens   |
| 48+ GB         | 256,000 tokens  |

### Fix Options (pick one)

**Option 1: Env var (recommended)**
```bash
OLLAMA_CONTEXT_LENGTH=64000 ollama serve
```

**Option 2: systemd**
```bash
sudo systemctl edit ollama.service
# Add: Environment="OLLAMA_CONTEXT_LENGTH=64000"
sudo systemctl daemon-reload && sudo systemctl restart ollama
```

**Option 3: Modelfile (persistent per-model)**
```bash
echo -e "FROM qwen2.5-coder:32b\nPARAMETER num_ctx 64000" > Modelfile
ollama create qwen2.5-coder-64k -f Modelfile
```

**Verify:**
```bash
ollama ps
# CONTEXT column should show 64000
```

## Notes
- You CANNOT set context length via the OpenAI-compatible API (`/v1/chat/completions`)
- Must be configured server-side or via Modelfile
- This is the #1 source of confusion when integrating Ollama with Hermes
- Tool calling supported since Ollama 0.3.x (native on Llama 3.x, Qwen 2.5, Mistral, Hermes)