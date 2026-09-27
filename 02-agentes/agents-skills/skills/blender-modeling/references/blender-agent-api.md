# blender-agent API 参考

## 安装

```bash
git clone https://github.com/FlSnowfluff/blender-agent.git
cd blender-agent
pip install -e .
```

---

## CLI

```
blender-agent [description] [options]

输入（至少一项）：
  description           自然语言描述（位置参数，可省略）
  -i, --image PATH/URL  参考图片：本地路径或 http(s) URL

输出：
  -o, --output PATH     输出 .glb 文件路径
  --save-script PATH    同时保存生成的 .py 脚本
  --dry-run             只打印脚本，不运行 Blender

模型 / API：
  --model MODEL         LLM 模型名（默认：gpt-4o）
  --base-url URL        OpenAI 兼容 API 地址
  --api-key KEY         API Key（默认读 OPENAI_API_KEY 环境变量）

执行：
  --blender PATH        Blender 可执行文件路径（可用 BLENDER_PATH 环境变量代替）
  --retries N           自纠错重试次数（默认：2）
```

### 常用示例

```bash
# 文字建模
blender-agent "a low-poly mountain with snow cap" -o mountain.glb

# 图片建模
blender-agent --image chair.jpg -o chair.glb

# 文字 + 图片
blender-agent "low-poly stylized" --image chair.jpg -o chair.glb

# 使用 DeepSeek
blender-agent "a wooden table" -o table.glb \
  --base-url https://api.deepseek.com/v1 \
  --model deepseek-chat \
  --api-key $DEEPSEEK_API_KEY

# 离线（Ollama + llava）
blender-agent --image mug.jpg -o mug.glb \
  --base-url http://localhost:11434/v1 --model llava

# 只查看脚本
blender-agent "a red cube on a white plane" --dry-run
```

---

## Python API

### `BlenderAgent(api_key, base_url, model, max_retries)`

| 参数 | 类型 | 默认 | 说明 |
|---|---|---|---|
| `api_key` | str | `$OPENAI_API_KEY` | API Key |
| `base_url` | str | None（OpenAI） | 非 OpenAI 提供商的接口地址 |
| `model` | str | `"gpt-4o"` | 使用图片时须为视觉模型 |
| `max_retries` | int | `2` | 脚本报错后的自动重试次数 |

### `agent.run(description, image, output_path, blender_path, dry_run)`

| 参数 | 类型 | 说明 |
|---|---|---|
| `description` | str | 自然语言描述（与 image 至少一项） |
| `image` | str | 本地路径或 http(s) URL |
| `output_path` | str | 输出 .glb 路径 |
| `blender_path` | str | Blender 可执行文件路径 |
| `dry_run` | bool | True 则只返回脚本，不执行 |

返回值：`dict(script, output_path, success, error)`

### `agent.generate_script(description, image, error_context)`

只调用 LLM 生成脚本字符串，不执行 Blender。`error_context` 用于传入上次报错，触发自纠错。

---

## 支持的 API 提供商

| 提供商 | base_url | 视觉支持 |
|---|---|---|
| OpenAI | （默认） | ✅ gpt-4o |
| DeepSeek | `https://api.deepseek.com/v1` | ✅ deepseek-vl |
| Ollama 本地 | `http://localhost:11434/v1` | ✅ llava, bakllava |
| 其他 OpenAI 兼容接口 | 自定义 URL | 取决于模型 |
