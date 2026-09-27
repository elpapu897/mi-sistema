---
tool: Codex
session_id: 019ff95d-4f6a-7800-aa10-9f0840519f80
fecha: 2026-08-13 04:24
titulo: "homematiigonzzDescargasclaude video mainzip instal"
tags: [chat, agente, codex]
---

# 💬 homematiigonzzDescargasclaude video mainzip instal
> **Codex** · 2026-08-13 04:24 · `019ff95d-4f6a-7800-aa10-9f0840519f80`

---

### 🧑 Vos  <small>2026-08-13 04:24</small>

@"/home/matiigonzz/Descargas/claude-video-main.zip"
instala esta skill

### 🤖 Codex  <small>2026-08-13 04:24</small>

I'll take a look at the zip file first.

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: List zip contents
command: ls -la "/home/matiigonzz/Descargas/claude-video-main.zip" && unzip -l "/home/matiigonzz/Descargas/claude-video-main.zip"
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
-rw-r--r--. 1 matiigonzz matiigonzz 54360 ago  9 23:14 /home/matiigonzz/Descargas/claude-video-main.zip
Archive:  /home/matiigonzz/Descargas/claude-video-main.zip
83da59fa78c3eee9e20f515fe75c438bb5166efd
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  06-30-2026 04:20   claude-video-main/
        0  06-30-2026 04:20   claude-video-main/.claude-plugin/
      608  06-30-2026 04:20   claude-video-main/.claude-plugin/marketplace.json
      612  06-30-2026 04:20   claude-video-main/.claude-plugin/plugin.json
        0  06-30-2026 04:20   claude-video-main/.codex-plugin/
     1663  06-30-2026 04:20   claude-video-main/.codex-plugin/plugin.json
      623  06-30-2026 04:20   claude-video-main/.skillignore
     3660  06-30-2026 04:20   claude-video-main/AGENTS.md
     5117  06-30-2026 04:20   claude-video-main/CHANGELOG.md
       11  06-30-2026 04:20   claude-video-main/CLAUDE.md
     1072  06-30-2026 04:20   claude-video-main/LICENSE
    19510  06-30-2026 04:20   claude-video-main/README.md
        0  06-30-2026 04:20   claude-video-main/hooks/
      279  06-30-2026 04:20   claude-video-main/hooks/hooks.json
        0  06-30-2026 04:20   claude-video-main/hooks/scripts/
     2009  06-30-2026 04:20   claude-video-main/hooks/scripts/check-setup.sh
        0  06-30-2026 04:20   claude-video-main/skills/
        0  06-30-2026 04:20   claude-video-main/skills/watch/
    21807  06-30-2026 04:20   claude-video-main/skills/watch/SKILL.md
        0  06-30-2026 04:20   claude-video-main/skills/watch/scripts/
     2108  06-30-2026 04:20   claude-video-main/skills/watch/scripts/config.py
     5454  06-30-2026 04:20   claude-video-main/skills/watch/scripts/download.py
    26346  06-30-2026 04:20   claude-video-main/skills/watch/scripts/frames.py
    12080  06-30-2026 04:20   claude-video-main/skills/watch/scripts/setup.py
     2897  06-30-2026 04:20   claude-video-main/skills/watch/scripts/transcribe.py
    16482  06-30-2026 04:20   claude-video-main/skills/watch/scripts/watch.py
    17046  06-30-2026 04:20   claude-video-main/skills/watch/scripts/whisper.py
---------                     -------
   139384                     27 files
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Inspect Claude config dirs
command: ls -la ~/.claude/ 2>/dev/null; echo "--- skills"; ls -la ~/.claude/skills/ 2>/dev/null; echo "--- plugins"; ls -la ~/.claude/plugins/ 2>/dev/null
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
total 52
drwxr-xr-x. 1 matiigonzz matiigonzz   468 ago  9 23:15 .
drwx------. 1 matiigonzz matiigonzz   788 ago  9 23:16 ..
drwxr-xr-x. 1 matiigonzz matiigonzz   330 ago  9 23:15 backups
drwxr-xr-x. 1 matiigonzz matiigonzz    24 ago  4 21:05 cache
-rw-------. 1 matiigonzz matiigonzz 18390 ago  4 23:47 .credentials.json
drwxr-xr-x. 1 matiigonzz matiigonzz     0 ago  4 21:05 downloads
-rw-------. 1 matiigonzz matiigonzz    69 ago  4 23:51 .env
drwxr-xr-x. 1 matiigonzz matiigonzz    72 ago  5 00:05 file-history
-rw-------. 1 matiigonzz matiigonzz  2329 ago  5 00:57 history.jsonl
-rw-r--r--. 1 matiigonzz matiigonzz    24 ago  9 23:13 .last-cleanup
-rw-r--r--. 1 matiigonzz matiigonzz   116 ago  9 23:01 mcp-needs-auth-cache.json
drwxr-xr-x. 1 matiigonzz matiigonzz   122 ago  9 23:15 plugins
-rw-r--r--. 1 matiigonzz matiigonzz  5723 ago  5 01:01 PLUGINS_SETUP.md
drwxr-xr-x. 1 matiigonzz matiigonzz    78 ago  4 21:27 projects
drwxr-xr-x. 1 matiigonzz matiigonzz  2304 ago  9 23:16 session-env
drwx------. 1 matiigonzz matiigonzz   118 ago  9 23:16 sessions
-rw-------. 1 matiigonzz matiigonzz   504 ago  9 23:15 settings.json
-rw-------. 1 matiigonzz matiigonzz   112 ago  5 01:03 settings.json.backup.20260805_010139
drwxr-xr-x. 1 matiigonzz matiigonzz   444 ago  9 23:16 shell-snapshots
drwxr-xr-x. 1 matiigonzz matiigonzz  1248 jul 31 04:13 skills
drwxr-xr-x. 1 matiigonzz matiigonzz   760 ago  9 21:27 telemetry
--- skills
total 0
drwxr-xr-x. 1 matiigonzz matiigonzz 1248 jul 31 04:13 .
drwxr-xr-x. 1 matiigonzz matiigonzz  468 ago  9 23:15 ..
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 ab-testing
drwxr-xr-x. 1 matiigonzz matiigonzz   58 jul 30 02:26 ad-creative
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 ads
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 ai-seo
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 analytics
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 aso
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 attribution
drwxr-xr-x. 1 matiigonzz matiigonzz   36 jul 31 04:13 banner-design
drwxr-xr-x. 1 matiigonzz matiigonzz   68 jul 31 04:13 brand
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 churn-prevention
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 cold-email
drwxr-xr-x. 1 matiigonzz matiigonzz   26 jul 30 02:26 co-marketing
drwxr-xr-x. 1 matiigonzz matiigonzz   26 jul 30 02:26 community-marketing
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 competitor-profiling
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 competitors
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 content-strategy
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 copy-editing
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 copywriting
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 cro
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 customer-research
drwxr-xr-x. 1 matiigonzz matiigonzz   58 jul 31 04:13 design
drwxr-xr-x. 1 matiigonzz matiigonzz   76 jul 31 04:13 design-system
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 directory-submissions
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 emails
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 free-tools
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 image
drwxr-xr-x. 1 matiigonzz matiigonzz   26 jul 30 02:26 influencer-marketing
drwxr-xr-x. 1 matiigonzz matiigonzz   26 jul 30 02:26 launch
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 lead-magnets
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 marketing-council
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 marketing-ideas
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 marketing-loops
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 marketing-plan
drwxr-xr-x. 1 matiigonzz matiigonzz   26 jul 30 02:26 marketing-psychology
drwxr-xr-x. 1 matiigonzz matiigonzz   36 jul 30 02:26 offers
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 02:26 onboarding
drwxr-xr-x. 1 matiigonzz matiigonzz   46 jul 30 0...
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Check installed plugins state
command: cat ~/.claude/plugins/installed_plugins.json; echo "---"; cat ~/.claude/plugins/known_marketplaces.json; echo "--- mkt dir"; ls -R ~/.claude/plugins/marketplaces | head -40; echo "--- data"; ls -R ~/.claude/plugins/data | head -40
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
{
  "version": 2,
  "plugins": {
    "ui-ux-pro-max@local-desktop-app-uploads": [
      {
        "scope": "user",
        "installPath": "/home/matiigonzz/.claude/plugins/marketplaces/local-desktop-app-uploads/ui-ux-pro-max",
        "version": "2.13.0",
        "installedAt": "2026-08-09T07:02:48.506Z",
        "lastUpdated": "2026-08-09T07:02:48.506Z"
      }
    ],
    "watch@local-desktop-app-uploads": [
      {
        "scope": "user",
        "installPath": "/home/matiigonzz/.claude/plugins/marketplaces/local-desktop-app-uploads/watch",
        "version": "0.2.0",
        "installedAt": "2026-08-10T02:15:00.498Z",
        "lastUpdated": "2026-08-10T02:15:00.498Z"
      }
    ]
  }
}---
{
  "claude-plugins-official": {
    "source": {
      "source": "github",
      "repo": "anthropics/claude-plugins-official"
    },
    "installLocation": "/home/matiigonzz/.claude/plugins/marketplaces/claude-plugins-official",
    "lastUpdated": "2026-08-05T02:46:01.093Z"
  },
  "local-desktop-app-uploads": {
    "source": {
      "source": "directory",
      "path": "/home/matiigonzz/.claude/plugins/marketplaces/local-desktop-app-uploads"
    },
    "installLocation": "/home/matiigonzz/.claude/plugins/marketplaces/local-desktop-app-uploads",
    "lastUpdated": "2026-08-05T03:53:32.213Z"
  }
}--- mkt dir
/home/matiigonzz/.claude/plugins/marketplaces:
claude-plugins-official
local-desktop-app-uploads

/home/matiigonzz/.claude/plugins/marketplaces/claude-plugins-official:
external_plugins
LICENSE
plugins
README.md

/home/matiigonzz/.claude/plugins/marketplaces/claude-plugins-official/external_plugins:
asana
context7
discord
fakechat
firebase
github
gitlab
greptile
imessage
laravel-boost
linear
playwright
serena
telegram
terraform

/home/matiigonzz/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/asana:

/home/matiigonzz/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/context7:

/home/matiigonzz/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/discord:
ACCESS.md
bun.lock
LICENSE
package.json
README.md
server.ts
skills

--- data
/home/matiigonzz/.claude/plugins/data:
pdf-viewer-inline
watch-inline
watch-local-desktop-app-uploads

/home/matiigonzz/.claude/plugins/data/pdf-viewer-inline:

/home/matiigonzz/.claude/plugins/data/watch-inline:

/home/matiigonzz/.claude/plugins/data/watch-local-desktop-app-uploads:
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Inspect local marketplace watch plugin
command: ls -la ~/.claude/plugins/marketplaces/local-desktop-app-uploads/; echo "=== watch"; ls -R ~/.claude/plugins/marketplaces/local-desktop-app-uploads/watch 2>/dev/null | head -40
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
total 0
drwx------. 1 matiigonzz matiigonzz  64 ago  9 23:15 .
drwxr-xr-x. 1 matiigonzz matiigonzz  96 ago  5 00:53 ..
drwx------. 1 matiigonzz matiigonzz  32 ago  9 23:15 .claude-plugin
drwxr-xr-x. 1 matiigonzz matiigonzz 398 ago  9 04:02 ui-ux-pro-max
drwxr-xr-x. 1 matiigonzz matiigonzz 192 ago  9 23:15 watch
=== watch
/home/matiigonzz/.claude/plugins/marketplaces/local-desktop-app-uploads/watch:
AGENTS.md
CHANGELOG.md
CLAUDE.md
hooks
LICENSE
README.md
skills

/home/matiigonzz/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/hooks:
hooks.json
scripts

/home/matiigonzz/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/hooks/scripts:
check-setup.sh

/home/matiigonzz/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/skills:
watch

/home/matiigonzz/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/skills/watch:
scripts
SKILL.md

/home/matiigonzz/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/skills/watch/scripts:
config.py
download.py
frames.py
setup.py
transcribe.py
watch.py
whisper.py
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Read setup check script and skill header
command: cd ~/.claude/plugins/marketplaces/local-desktop-app-uploads/watch && cat hooks/scripts/check-setup.sh; echo "=== SKILLMD head"; head -60 skills/watch/SKILL.md
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
#!/usr/bin/env bash
# SessionStart hook for /watch — one-line status so users know what's wired up.
# Silent on ready state to avoid spam. Points at the installer when something
# is missing.
set -euo pipefail

CONFIG_FILE="$HOME/.config/watch/.env"

# Warn if the secrets file has loose permissions.
if [[ -f "$CONFIG_FILE" ]]; then
  perms=$(stat -c '%a' "$CONFIG_FILE" 2>/dev/null || stat -f '%Lp' "$CONFIG_FILE" 2>/dev/null || echo "")
  if [[ -n "$perms" && "$perms" != "600" && "$perms" != "400" ]]; then
    echo "/watch: WARNING — $CONFIG_FILE has permissions $perms (should be 600)."
    echo "  Fix: chmod 600 $CONFIG_FILE"
  fi
fi

# Load API keys from the config file without exporting them.
read_key() {
  local name="$1"
  if [[ -n "${!name:-}" ]]; then
    echo "${!name}"
    return
  fi
  if [[ -f "$CONFIG_FILE" ]]; then
    awk -F= -v k="$name" '
      /^[[:space:]]*#/ { next }
      $1 == k {
        sub(/^[[:space:]]*/, "", $2); sub(/[[:space:]]*$/, "", $2);
        gsub(/^["'\'']|["'\'']$/, "", $2);
        print $2; exit
      }
    ' "$CONFIG_FILE"
  fi
}

HAS_FFMPEG=""
HAS_YTDLP=""
command -v ffmpeg >/dev/null 2>&1 && HAS_FFMPEG="yes"
command -v yt-dlp >/dev/null 2>&1 && HAS_YTDLP="yes"

HAS_GROQ="$(read_key GROQ_API_KEY)"
HAS_OPENAI="$(read_key OPENAI_API_KEY)"
SETUP_COMPLETE="$(read_key SETUP_COMPLETE)"

# Fully configured → silent (Claude can surface status on demand via --check).
if [[ "$SETUP_COMPLETE" == "true" && -n "$HAS_FFMPEG" && -n "$HAS_YTDLP" ]]; then
  exit 0
fi

# First-run / partially-configured → one-line hint.
if [[ -z "$HAS_FFMPEG" || -z "$HAS_YTDLP" ]]; then
  echo "/watch: needs ffmpeg + yt-dlp. Run \`python3 \$CLAUDE_PLUGIN_ROOT/skills/watch/scripts/setup.py\` once to install and scaffold config."
elif [[ -z "$HAS_GROQ" && -z "$HAS_OPENAI" ]]; then
  echo "/watch: ready for videos with native captions. Add GROQ_API_KEY (preferred) or OPENAI_API_KEY to ~/.config/watch/.env to unlock Whisper fallback."
else
  echo "/watch: ready."
fi
=== SKILLMD head
---
name: watch
version: "0.2.0"
description: Watch a video (URL or local path). Downloads with yt-dlp, extracts auto-scaled frames with ffmpeg, pulls the transcript from captions (or Whisper API fallback), and hands the result to Claude so it can answer questions about what's in the video.
argument-hint: "<video-url-or-path> [question]"
allowed-tools: Bash, Read, AskUserQuestion
homepage: https://github.com/bradautomates/claude-video
repository: https://github.com/bradautomates/claude-video
author: bradautomates
license: MIT
user-invocable: true
---

# /watch

You don't have a video input; this skill gives you one. A Python script gets captions first, optionally downloads the video, extracts frames as JPEGs (scene-aware, or fast keyframes at `efficient` detail), gets a timestamped transcript (native captions first, then Whisper API as fallback), and prints frame paths. You then `Read` each frame path to see the images and combine them with the transcript to answer the user.

## Resolve `SKILL_DIR` (do this before any command)

Every `python3 ...` command below runs a bundled script under `SKILL_DIR/scripts/`. Set `SKILL_DIR` to the **absolute path of the directory containing THIS SKILL.md you just Read** — your harness told you that path in the Read result. The scripts are always a direct sibling of this file (`SKILL_DIR/scripts/watch.py`), in every install layout:

```
Read ~/.claude/plugins/cache/claude-video/watch/<ver>/skills/watch/SKILL.md → SKILL_DIR=…/skills/watch
Read ~/.codex/skills/watch/SKILL.md                                          → SKILL_DIR=~/.codex/skills/watch
Read ~/.agents/skills/watch/SKILL.md                                         → SKILL_DIR=~/.agents/skills/watch
```

Substitute that literal path for `${SKILL_DIR}` in every command. This works on every harness (Claude Code, Codex, Cursor, Gemini CLI, …) without relying on any harness-specific environment variable. Guard once at the start of a run:

```bash
SKILL_DIR="...
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

El plugin ya quedó instalado (la app lo cargó desde el zip). Ahora completo el setup de dependencias.

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Run watch setup preflight
command: python3 ~/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/skills/watch/scripts/setup.py --json 2>&1 | tail -40
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
{
  "status": "needs_key",
  "can_proceed": false,
  "first_run": true,
  "setup_complete": false,
  "missing_binaries": [],
  "whisper_backend": null,
  "has_api_key": false,
  "config_file": "/home/matiigonzz/.config/watch/.env",
  "watch_detail": "balanced",
  "platform": "Linux"
}
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Check config file and preference options
command: ls -la ~/.config/watch/ 2>/dev/null && cat ~/.config/watch/.env; echo "=== binaries"; command -v ffmpeg yt-dlp; echo "=== prefs section"; grep -n -A 40 "watch-preference\|Preference\|WATCH_DETAIL" ~/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/skills/watch/SKILL.md | head -80
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
=== binaries
/usr/bin/ffmpeg
/home/matiigonzz/.local/bin/yt-dlp
=== prefs section
55:  3. Encourage a Whisper API key and ask the watch-preference questions below, then write the selected values into `~/.config/watch/.env` and set `SETUP_COMPLETE=true`.
56-- **`can_proceed: false` and `first_run: false`** → setup was finished before but the environment regressed (e.g. `missing_binaries` after an OS change). Run the installer to remediate, then proceed. Don't re-ask preferences.
57-
58-A missing Whisper key is *encouraged to fix, not required*: on a genuine first run `status` will read `needs_key` even when binaries are present — that's your cue to encourage a key, not a blocker.
59-
60-On follow-up `/watch` calls in the same session, use the silent check:
61-
62-```bash
63-python3 "${SKILL_DIR}/scripts/setup.py" --check
64-```
65-
66-This is a <100ms lookup. Exit 0 means /watch can run — this **includes a user who finished setup without a Whisper key** (keyless is allowed). On exit 0 the script emits **nothing** — proceed to Step 1 without comment. **Do NOT announce "setup is complete" to the user** — they don't need a status message on every turn. The only acceptable user-visible output from Step 0 is when remediation is required.
67-
68-On non-zero exit, follow the table:
69-
70-| Exit | Meaning | Action |
71-|------|---------|--------|
72-| `2` | Missing binaries (`ffmpeg` / `ffprobe` / `yt-dlp`) | Run installer |
73-| `3` | Genuine first run with no Whisper API key | Run installer to scaffold `.env`, then encourage a key (the user may decline — proceed with `--no-whisper`) |
74-| `4` | Both missing | Run installer, then encourage a key |
75-
76-Exit `3` only fires before the user has completed setup. Once `SETUP_COMPLETE=true` is written, a keyless install returns exit 0 and is never nagged again.
77-
78-The installer is idempotent — safe to re-run:
79-
80-```bash
81-python3 "${SKILL_DIR}/scripts/setup.py"
82-```
83-
84-On macOS with Homebrew, it auto-installs `ffmpeg` and `yt-dlp`. On Linux/Windows, it prints the exact install commands for the user to run. It scaffolds `~/.config/watch/.env` with commented placeholders and default watch settings at `0600` perms.
85-
86-**If an API key is still missing after install:** use `AskUserQuestion` to ask the user whether they have a Groq API key (preferred — cheaper, faster) or an OpenAI key. Then write it into `~/.config/watch/.env` — set the matching `GROQ_API_KEY=...` or `OPENAI_API_KEY=...` line. If they don't want to set up Whisper, proceed with `--no-whisper` and tell them videos without native captions will come back frames-only.
87-
88-**First-run watch preference:** after the installer has scaffolded `~/.config/watch/.env`, use `AskUserQuestion` to ask one question:
89-
90-- Default detail (one dial). Present these as `AskUserQuestion` options in this exact order — lightest to heaviest — and keep `(recommended)` on `balanced` even though it is not first (do **not** reorder to put the recommended option first):
91-  - `transcript` — no frames at all, transcript only (skips video download when captions exist).
92-  - `efficient` — fast keyframe pass (cap 50).
93-  - `balanced` (recommended) — scene-aware frames (cap 100, default).
94-  - `token-burner` — scene-aware, uncapped (maximum fidelity; high token cost).
95-
--
99:WATCH_DETAIL=balanced
100-```
101-
102-Use the user's selected value. If they skip the question, keep the recommended default. Once dependencies, the API-key choice, and this preference are handled, write or update `SETUP_COMPLETE=true` in the same file. Do not ask this preference question again when `SETUP_COMPLETE=true`.
103-
104-**Structured mode (optional):** `python3 "${SKILL_DIR}/scripts/setup.py" --json` emits `{status, can_proceed, first_run, setup_complete, missing_binaries, whisper_backend, has_api_key, config_file, watch_detail, platform}` where `status` is one of `ready | needs_install | needs_key | needs_install_and_key`. `status` describe...
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Run installer to scaffold config
command: python3 ~/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/skills/watch/scripts/setup.py 2>&1 | tail -30; echo "=== env"; ls -l ~/.config/watch/.env && cat ~/.config/watch/.env
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
[setup] created config: /home/matiigonzz/.config/watch/.env

[setup] one step left: add a Whisper API key.

  Edit /home/matiigonzz/.config/watch/.env and set either:
    GROQ_API_KEY=...    (preferred — cheaper, faster; get one at console.groq.com/keys)
    OPENAI_API_KEY=...  (fallback; get one at platform.openai.com/api-keys)

  Without a key, /watch still works but videos without captions come back frames-only.
=== env
-rw-------. 1 matiigonzz matiigonzz 815 ago  9 23:16 /home/matiigonzz/.config/watch/.env
# /watch API configuration
#
# Whisper transcription fallback — used only when yt-dlp cannot get captions
# (or when you point /watch at a local file with no subtitles).
#
# Groq is preferred: it runs whisper-large-v3 at a fraction of OpenAI's price
# and is faster in practice. OpenAI is the compatible fallback.
#
# Get a Groq key:  https://console.groq.com/keys
# Get an OpenAI key:  https://platform.openai.com/api-keys
#
# Leave both blank to disable Whisper — /watch will still work, but videos
# without native captions will come back frames-only.

GROQ_API_KEY=
OPENAI_API_KEY=

# Default watch behavior (the /watch first-run wizard sets this for you).
# Allowed values: transcript | efficient | balanced | token-burner
# Keep the value on its own line with no trailing comment.
# WATCH_DETAIL=balanced
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

Ya está instalada y las dependencias (ffmpeg + yt-dlp) están presentes. Falta cerrar dos preferencias del primer arranque:

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: AskUserQuestion]
input: {"questions":[{"question":"¿Querés configurar una API key para Whisper (transcripción cuando el video no tiene subtítulos propios)?","header":"Whisper","multiSelect":false,"options":[{"label":"Sí, tengo Groq","description":"Groq es la recomendada: más barata y rápida (whisper-large-v3). Me pasás la key y la escribo en ~/.config/watch/.env con permisos 600."},{"label":"Sí, tengo OpenAI","description":"Usa la API de OpenAI como fallback. Me pasás la key y la guardo en el mismo archivo."},{"label":"No por ahora","description":"/watch igual funciona: usa subtítulos nativos cuando existen. Los videos sin subtítulos vuelven solo con frames (sin transcripción)."}]},{"question":"¿Qué nivel de detalle por defecto querés al mirar videos?","header":"Detalle","multiSelect":false,"options":[{"label":"transcript","description":"Sin frames, solo transcripción. Lo más barato en tokens; ni descarga el video si hay subtítulos."},{"label":"efficient","description":"Pasada rápida de keyframes (máx 50 frames). Buen equilibrio si mirás videos largos."},{"label":"balanced (recomendado)","description":"Frames por escena, máx 100. Es el default y el mejor balance calidad/costo."},{"label":"token-burner","description":"Frames por escena sin límite. Máxima fidelidad pero costo de tokens muy alto."}]}]}
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
Your questions have been answered: "¿Querés configurar una API key para Whisper (transcripción cuando el video no tiene subtítulos propios)?"="Sí, tengo Groq", "¿Qué nivel de detalle por defecto querés al mirar videos?"="balanced (recomendado)". You can now continue with these answers in mind.
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Set detail preference and mark setup complete
command: python3 - <<'EOF'
from pathlib import Path
p = Path.home()/".config/watch/.env"
t = p.read_text()
t = t.replace("# WATCH_DETAIL=balanced", "WATCH_DETAIL=balanced")
if "SETUP_COMPLETE" not in t:
    t = t.rstrip("\n") + "\nSETUP_COMPLETE=true\n"
p.write_text(t)
p.chmod(0o600)
print(t[-260:])
EOF
echo "=== check"; python3 ~/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/skills/watch/scripts/setup.py --json
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
OPENAI_API_KEY=

# Default watch behavior (the /watch first-run wizard sets this for you).
# Allowed values: transcript | efficient | balanced | token-burner
# Keep the value on its own line with no trailing comment.
WATCH_DETAIL=balanced
SETUP_COMPLETE=true

=== check
{
  "status": "needs_key",
  "can_proceed": true,
  "first_run": false,
  "setup_complete": true,
  "missing_binaries": [],
  "whisper_backend": null,
  "has_api_key": false,
  "config_file": "/home/matiigonzz/.config/watch/.env",
  "watch_detail": "balanced",
  "platform": "Linux"
}
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

Listo. La skill **`/watch`** quedó instalada y operativa.

**Estado:**
- Plugin `watch@local-desktop-app-uploads` v0.2.0 instalado en `~/.claude/plugins/marketplaces/local-desktop-app-uploads/watch`
- `ffmpeg` ✅ (`/usr/bin/ffmpeg`) y `yt-dlp` ✅ (`~/.local/bin/yt-dlp`) — ya los tenías
- Config creada en `~/.config/watch/.env` con permisos `600`
- `WATCH_DETAIL=balanced` (frames por escena, máx 100) y `SETUP_COMPLETE=true`
- Falta solo tu key de Groq

**Para cargar tu Groq key** (así no la pegás en el chat, corré esto y reemplazá `gsk_tu_key_aca`):

```bash
sed -i 's|^GROQ_API_KEY=.*|GROQ_API_KEY=gsk_tu_key_aca|' ~/.config/watch/.env && chmod 600 ~/.config/watch/.env && grep -c '^GROQ_API_KEY=gsk' ~/.config/watch/.env
```

Si devuelve `1`, quedó bien.

**Cómo se usa:**

```bash
/watch https://youtu.be/VIDEO_ID de qué habla el video
```

También funciona con archivos locales (`/watch ~/Videos/clip.mp4 ¿qué pasa al final?`). Descarga con yt-dlp, extrae frames con ffmpeg, saca la transcripción de los subtítulos nativos (y si no hay, cae a Whisper vía Groq una vez que cargues la key) y yo leo los frames para responderte.

Un detalle: rinde mejor con videos de menos de 10 minutos — arriba de eso el muestreo de frames se vuelve muy espaciado. Si tenés uno largo, conviene que me digas qué tramo te interesa.

### 🧑 Vos  <small>2026-08-13 04:24</small>

xai-YCYl5rgiDFYx7BGtnVv7LYBbyGcGBRHS4UdH1WEAj0y3yVWy1esrCPrvncbupUF7cDHFLEv9zbnKjDhm

### 🤖 Codex  <small>2026-08-13 04:24</small>

Pará un segundo antes de guardarlo: esa key es de **xAI** (`xai-...`), no de Groq. Son servicios distintos que se confunden fácil por el nombre. Dejame verificar qué acepta el script.

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Check supported whisper backends
command: grep -n "api.groq\|api.openai\|BASE_URL\|base_url\|GROQ_API_KEY\|OPENAI_API_KEY\|x.ai\|XAI" ~/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/skills/watch/scripts/whisper.py ~/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/skills/watch/scripts/config.py | head -30
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
/home/matiigonzz/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/skills/watch/scripts/whisper.py:29:GROQ_ENDPOINT = "https://api.groq.com/openai/v1/audio/transcriptions"
/home/matiigonzz/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/skills/watch/scripts/whisper.py:32:OPENAI_ENDPOINT = "https://api.openai.com/v1/audio/transcriptions"
/home/matiigonzz/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/skills/watch/scripts/whisper.py:98:    candidates = (("GROQ_API_KEY", "groq"), ("OPENAI_API_KEY", "openai"))
/home/matiigonzz/.claude/plugins/marketplaces/local-desktop-app-uploads/watch/skills/watch/scripts/whisper.py:432:            "No Whisper API key available. Set GROQ_API_KEY (preferred) or OPENAI_API_KEY "
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

No la guardé. Dos cosas:

**1. Esa key no sirve para `/watch`.** El script tiene los endpoints hardcodeados y solo soporta dos:
- `https://api.groq.com/openai/v1/audio/transcriptions` → `GROQ_API_KEY`
- `https://api.openai.com/v1/audio/transcriptions` → `OPENAI_API_KEY`

Una key de xAI (Grok) no autentica contra ninguno de los dos, y además xAI no expone un endpoint de transcripción de audio tipo Whisper. Aunque la pegara en el archivo, la transcripción fallaría con un 401 y volverías a quedar solo con frames.

**2. Rotá esa key.** La pegaste en el chat, así que consideralá comprometida. Andá a [console.x.ai](https://console.x.ai) → API Keys, borrá esa y generá una nueva. Es un trámite de 30 segundos y te evita que alguien te queme créditos.

**Para lo que sí necesitás:** una key de Groq en [console.groq.com/keys](https://console.groq.com/keys). Tiene tier gratuito y las keys arrancan con `gsk_`. Cuando la tengas, corré esto reemplazando el placeholder (no hace falta que me la pegues):

```bash
sed -i 's|^GROQ_API_KEY=.*|GROQ_API_KEY=gsk_TU_KEY|' ~/.config/watch/.env && chmod 600 ~/.config/watch/.env && grep -c '^GROQ_API_KEY=gsk' ~/.config/watch/.env
```

Mientras tanto `/watch` ya funciona igual para cualquier video con subtítulos nativos — que en YouTube es la enorme mayoría. La key de Groq solo entra en juego como fallback cuando no hay subtítulos (videos de X, TikTok, archivos locales sin pista de subtítulos).

### 🧑 Vos  <small>2026-08-13 04:24</small>

esa es la aplicación que me dio creo, esa es la API que me dio Grok. Grok, API, es la API Key. Es la que me dio boludo, qué gracias.

### 🤖 Codex  <small>2026-08-13 04:24</small>

Te creo — no estoy diciendo que la key sea trucha ni inventada. Es una key real que te dio Grok. El problema es otro y es una trampa de nombres genuinamente cruel:

- **Grok** = xAI, el chatbot de Musk. Es la tuya (`xai-...`).
- **Groq** = otra empresa, hace chips de inferencia. Su key arranca con `gsk_`.

Se escriben igual salvo una letra y no tienen nada que ver entre sí. Dejame probarlo en vez de discutirlo:

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_call: Bash]
description: Test key against xAI and Groq APIs
command: K="xai-YCYl5rgiDFYx7BGtnVv7LYBbyGcGBRHS4UdH1WEAj0y3yVWy1esrCPrvncbupUF7cDHFLEv9zbnKjDhm"
echo "=== contra xAI (su dueño real) ==="
curl -s -o /tmp/xai.json -w "HTTP %{http_code}\n" https://api.x.ai/v1/models -H "Authorization: Bearer $K"
head -c 400 /tmp/xai.json; echo
echo "=== contra Groq (lo que /watch necesita) ==="
curl -s -o /tmp/groq.json -w "HTTP %{http_code}\n" https://api.groq.com/openai/v1/models -H "Authorization: Bearer $K"
head -c 400 /tmp/groq.json; echo
[/external_agent_tool_call]

### 🤖 Codex  <small>2026-08-13 04:24</small>

[external_agent_tool_result]
=== contra xAI (su dueño real) ===
HTTP 403
{"code":"permission-denied","error":"Your team ef6f1569-8764-415e-9132-9c5b6ed67aa4 has either used all available credits or reached its monthly spending limit. To continue making API requests, please purchase more credits or raise your spending limit."}
=== contra Groq (lo que /watch necesita) ===
HTTP 401
{"error":{"message":"Invalid API Key","type":"invalid_request_error","code":"invalid_api_key"}}
[/external_agent_tool_result]

### 🤖 Codex  <small>2026-08-13 04:24</small>

Ahí está, en blanco sobre negro:

- **xAI la reconoce** (HTTP 403, no 401): la key es tuya y es válida. Pero tu equipo se quedó sin créditos / llegó al límite mensual de gasto.
- **Groq la rechaza** (HTTP 401 `invalid_api_key`): no la conoce, porque es otra empresa.

Así que no es que yo no quiera usarla — es que hay dos paredes, no una. Aunque xAI tuviera endpoint de transcripción (no lo tiene, solo chat e imágenes), la cuenta está sin créditos igual.

Lo bueno: **Groq es gratis para esto.** Andá a [console.groq.com/keys](https://console.groq.com/keys), entrás con Google, creás la key y listo — el tier gratuito cubre `whisper-large-v3` de sobra para mirar videos. Te va a salir algo tipo `gsk_...`:

```bash
sed -i 's|^GROQ_API_KEY=.*|GROQ_API_KEY=gsk_TU_KEY|' ~/.config/watch/.env && chmod 600 ~/.config/watch/.env && grep -c '^GROQ_API_KEY=gsk' ~/.config/watch/.env
```

Y rotá igual la de xAI cuando puedas, que quedó escrita en el chat.

Igual, no te bloquea nada ahora mismo: tirame un link de YouTube y `/watch` lo procesa con los subtítulos nativos, sin necesidad de ninguna key. La de Groq es solo para videos que no tienen subtítulos.
