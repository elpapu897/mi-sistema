---
tool: Codex
session_id: 01a09d3e-6f2a-7ed0-adbe-9c89e8ee2fa4
fecha: 2026-09-14 00:09
titulo: "como puedo conectar el mcp de httpsmcpfacebookcoma"
tags: [chat, agente, codex]
---

# 💬 como puedo conectar el mcp de httpsmcpfacebookcoma
> **Codex** · 2026-09-14 00:09 · `01a09d3e-6f2a-7ed0-adbe-9c89e8ee2fa4`

---

### 🧑 Vos  <small>2026-09-14 00:09</small>

como puedo conectar el mcp de [https://mcp.facebook.com/ads](https://mcp.facebook.com/ads)  en codex

### 🤖 Codex  <small>2026-09-14 00:09</small>

Voy a verificar el formato actual de configuración MCP de Codex y qué tipo de autenticación exige ese endpoint de Meta; así te doy pasos que funcionen en esta app, no una receta genérica. Para eso uso la skill oficial `openai-docs`.

### 🤖 Codex  <small>2026-09-14 00:09</small>

El endpoint respondió `405 Method Not Allowed` a una visita web normal, algo compatible con un servidor MCP que espera el transporte/protocolo MCP y no una página HTML. Ahora confirmo la sintaxis exacta de tu CLI instalada y si ya existe una entrada con ese nombre.

### 🤖 Codex  <small>2026-09-14 00:10</small>

La forma más directa es desde la terminal integrada de Codex:

```bash
codex mcp add facebook-ads --url https://mcp.facebook.com/ads
codex mcp login facebook-ads
```

El segundo comando debería abrir el navegador para autenticarte con Meta. Después verificá la conexión:

```bash
codex mcp list
```

Finalmente, reiniciá Codex para que cargue las herramientas nuevas. La configuración queda guardada en `~/.codex/config.toml` y es compartida por Codex Desktop, CLI y la extensión del IDE en el mismo equipo, según la [documentación oficial de MCP para Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli).

También podés configurarlo manualmente:

```toml
[mcp_servers.facebook_ads]
url = "https://mcp.facebook.com/ads"
auth = "oauth"
default_tools_approval_mode = "writes"
```

Luego ejecutás:

```bash
codex mcp login facebook_ads
```

Notas:

- Que la URL muestre `405 Method Not Allowed` al abrirla normalmente en el navegador no significa que esté caída: es un endpoint MCP, no una página web.
- Tu cuenta de Meta debe tener acceso al Business Portfolio y a las cuentas publicitarias correspondientes.
- `default_tools_approval_mode = "writes"` hace que Codex te pida confirmación antes de ejecutar herramientas que modifiquen campañas.
- Tu instalación actual (`codex-cli 0.154.0-alpha.6`) ya soporta servidores HTTP y OAuth.
