# Credenciales

Inventario de **qué** credenciales existen, **dónde** van y **cómo** regenerarlas
si dejaron de funcionar.

> Este documento no contiene ni un solo valor secreto. Solo nombres de variables
> y nombres de servicios. Los valores están cifrados en
> `99-secretos/secretos.tar.gpg`.

---

## Cómo recuperarlas

```bash
bash scripts/descifrar-secretos.sh
```

Pide la passphrase, y devuelve cada archivo a su lugar con los permisos
correctos. Las claves SSH quedan en `600`, que es obligatorio: con permisos más
abiertos SSH las ignora sin explicar por qué.

Antes de confiar en el paquete, verificá que abre:

```bash
gpg -d 99-secretos/secretos.tar.gpg | tar t
```

---

## Qué hay en el paquete cifrado

### Claves SSH

| Archivo | Va a | Permisos | Para qué |
|---|---|:--:|---|
| `gonvra_server` | `~/.ssh/gonvra_server` | `600` | Servidor GONVRA. Configurado como host `gonvra-srv`, usuario `gonvra`. |
| `gonvra_server.pub` | `~/.ssh/gonvra_server.pub` | `644` | Pública del anterior |
| `gonvra_vps` | `~/.ssh/gonvra_vps` | `600` | VPS de GONVRA |
| `gonvra_vps.pub` | `~/.ssh/gonvra_vps.pub` | `644` | Pública del anterior |
| `config` | `~/.ssh/config` | `600` | Hosts y qué clave usa cada uno |
| `known_hosts` | `~/.ssh/known_hosts` | `644` | Fingerprints conocidos |

Probar el acceso:

```bash
ssh gonvra-srv            # usa la config, no hace falta -i
ssh -i ~/.ssh/gonvra_vps <usuario>@<host>
```

**Si perdiste las claves**, no hay forma de recuperarlas: hay que generar un par
nuevo y autorizarlo desde el panel del proveedor o desde una sesión ya abierta.

```bash
ssh-keygen -t ed25519 -f ~/.ssh/gonvra_vps_nueva -C "tomexos-$(date +%Y%m)"
ssh-copy-id -i ~/.ssh/gonvra_vps_nueva <usuario>@<host>
```

### Tokens de agentes

| Archivo | Va a | Qué tiene |
|---|---|---|
| `claude/.credentials.json` | `~/.claude/.credentials.json` | OAuth de Claude.ai + **75 servidores MCP** con OAuth |
| `claude/.env` | `~/.claude/.env` | `GEMINI_API_KEY` |
| `claude/sessions/*.key` | `~/.claude/sessions/` | Claves de sesión |
| `codex/auth.json` | `~/.codex/auth.json` | `OPENAI_API_KEY` + tokens OAuth (id, access, refresh) |
| `hermes/.env` | `~/.hermes/.env` | 5 API keys + token de Telegram (detalle abajo) |
| `hermes/auth.json` | `~/.hermes/auth.json` | Autenticación de Hermes |
| `gemini/oauth_creds.json` | `~/.gemini/oauth_creds.json` | OAuth de Gemini / Antigravity |

### Claves de API en `.hermes/.env`

| Variable | Servicio | Dónde regenerarla |
|---|---|---|
| `GOOGLE_API_KEY` | Google AI | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) |
| `DEEPSEEK_API_KEY` | DeepSeek | [platform.deepseek.com](https://platform.deepseek.com/api_keys) |
| `KIMI_CN_API_KEY` | Moonshot / Kimi | [platform.moonshot.cn](https://platform.moonshot.cn) |
| `APINEX_API_KEY` | Apinex | Panel de Apinex |
| `TELEGRAM_BOT_TOKEN` | Bot de Telegram | [@BotFather](https://t.me/BotFather) → `/mybots` → API Token |

El resto de las variables de ese archivo (`BROWSERBASE_*`, `TERMINAL_*`,
`*_DEBUG`, `BROWSER_*`) son configuración, no secretos.

### En `.claude/.env`

| Variable | Servicio | Dónde regenerarla |
|---|---|---|
| `GEMINI_API_KEY` | Google AI Studio | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) |

---

## Lo que probablemente haya que re-autenticar igual

Los tokens OAuth suelen estar atados al dispositivo o vencen. Cambiar de sistema
operativo los invalida seguido. **Esto es normal y no significa que el backup
falló.**

| Qué | Cómo |
|---|---|
| Claude Code | `claude` y seguí el login del navegador |
| Codex | `codex login` |
| Gemini / Antigravity | login desde la app |
| GitHub CLI | `gh auth login` |
| Los 75 servidores MCP | Se re-autorizan solos al usarlos por primera vez |

Las **API keys** (`GEMINI_API_KEY`, `DEEPSEEK_API_KEY`, etc.) no vencen por
cambiar de máquina: esas se restauran y siguen funcionando.

---

## Los 75 servicios MCP con OAuth guardado

Agrupados por plugin. Si alguno pide login de nuevo, se resuelve en el momento.

| Plugin | Servicios |
|---|---|
| `bio-research` | biorender, owkin, synapse, wiley |
| `customer-support` | guru, hubspot, intercom |
| `data` | definite, hex |
| `engineering` | datadog, github, pagerduty |
| `finance` | bigquery |
| `legal` | atlassian, box, egnyte, slack |
| `marketing` | ahrefs, klaviyo, similarweb, supermetrics |
| `product-management` | amplitude, amplitude-eu, figma |
| `productivity` | linear |
| *(y el resto hasta 75)* | La lista completa está en el propio `.credentials.json` |

---

## Qué quedó sin cifrar, a propósito

Estos archivos están **en claro** en el repo porque no son secretos, pero es
bueno que lo sepas:

| Archivo | Por qué está en claro |
|---|---|
| `06-dotfiles/ssh/config` | Hosts, usuarios y rutas de claves. No hay material criptográfico, pero sí la IP y el usuario del servidor. |
| `06-dotfiles/ssh/*.pub` | Las claves públicas son públicas por diseño. |
| `07-historial-agentes/**` | El historial de conversaciones. **Si alguna vez pegaste una clave en un chat, quedó ahí.** Por eso el repo es privado. |

---

## Reglas

1. **La passphrase no tiene recuperación.** Si la perdés, el paquete es un
   archivo inútil. Guardala en un gestor de contraseñas, no en este repo.
2. **El repo tiene que quedar privado.** Aunque los secretos estén cifrados, el
   historial de conversaciones no lo está.
3. **Si sospechás que se filtró algo, rotá primero y preguntá después.** Las API
   keys se regeneran en dos minutos; un servidor comprometido no.
