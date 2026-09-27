---
tool: Codex
session_id: 01a09d40-f903-77c3-8a47-375fd5717d4a
fecha: 2026-09-14 00:11
titulo: "como conectsr el mcp de facebook en codex httpsmcp"
tags: [chat, agente, codex]
---

# 💬 como conectsr el mcp de facebook en codex httpsmcp
> **Codex** · 2026-09-14 00:11 · `01a09d40-f903-77c3-8a47-375fd5717d4a`

---

### 🧑 Vos  <small>2026-09-14 00:11</small>

como conectsr el mcp de facebook en codex [https://mcp.facebook.com/ads](https://mcp.facebook.com/ads)

### 🤖 Codex  <small>2026-09-14 00:11</small>

Voy a verificar el procedimiento actual de Codex y los requisitos específicos del endpoint de Meta, porque la configuración y el flujo OAuth pueden cambiar. Estoy usando la guía oficial de documentación de OpenAI para darte pasos compatibles con la versión actual.

### 🤖 Codex  <small>2026-09-14 00:12</small>

Codex admite este servidor como MCP remoto por HTTP y puede completar el inicio de sesión OAuth desde la app o la CLI. Estoy confirmando la sintaxis exacta instalada antes de pasarte los comandos.

### 🤖 Codex  <small>2026-09-14 00:13</small>

La forma más directa es desde la terminal:

```bash
codex mcp add facebook-ads --url https://mcp.facebook.com/ads
codex mcp login facebook-ads
```

El segundo comando abrirá el navegador para iniciar sesión en Meta y autorizar las cuentas publicitarias correspondientes.

Después:

```bash
codex mcp list
```

Reiniciá Codex y escribí `/mcp` para comprobar que `facebook-ads` aparece conectado.

También podés hacerlo desde la interfaz:

1. Abrí **Settings → MCP servers**.
2. Elegí **Add server**.
3. Nombre: `facebook-ads`.
4. Tipo: **Streamable HTTP**.
5. URL: `https://mcp.facebook.com/ads`.
6. Guardá, reiniciá Codex y presioná **Authenticate**.

Codex guarda esta configuración en `~/.codex/config.toml`. Debido a que las herramientas de Ads podrían modificar campañas o presupuesto, conviene mantener activadas las aprobaciones para operaciones de escritura.

Documentación oficial: [configurar servidores MCP en Codex](https://developers.openai.com/codex/mcp/).

### 🧑 Vos  <small>2026-09-14 00:21</small>

/facebook-ads

### 🤖 Codex  <small>2026-09-14 00:21</small>

`/facebook-ads` no es un comando de Codex. Usá:

```text
/mcp
```

Confirmá que `facebook-ads` figure como conectado y después pedime en lenguaje natural, por ejemplo:

> Mostrame el rendimiento de mis campañas de Meta Ads de los últimos 7 días.

### 🧑 Vos  <small>2026-09-14 00:22</small>

/face No me deja apretar el botón, boludo. Tipo, no me deja apretarlo. pero sí que me aparece tipo habilitado. eso es lo que pasa.

### 🤖 Codex  <small>2026-09-14 00:22</small>

Ahí entendí: que aparezca **habilitado** no significa que cree un botón o comando `/facebook-ads`. Voy a revisar el estado real del servidor en tu Codex para distinguir si está conectado, pendiente de OAuth o solamente configurado.

### 🤖 Codex  <small>2026-09-14 00:22</small>

Ya encontré el punto: está registrado como **enabled**, pero figura **Auth: Unknown**, no como autenticado. Por eso `/face` no aparece y el botón no sirve. Voy a probar el inicio de sesión por CLI, que evita ese problema de la interfaz; si Meta abre OAuth, solo tendrás que autorizarlo en el navegador.

### 🤖 Codex  <small>2026-09-14 00:32</small>

La interfaz no es el problema principal: Meta rechazó el registro OAuth dinámico con `invalid_client_metadata`. Voy a probar el otro método que Codex soporta para servidores remotos, CIMD, antes de concluir que Meta exige un Client ID registrado manualmente.

### 🤖 Codex  <small>2026-09-14 00:33</small>

Ya encontré el problema: `facebook-ads` está habilitado, pero aparece como **Auth: Unknown**. Probé ambos métodos automáticos de OAuth:

- DCR: Meta responde `invalid_client_metadata`.
- CIMD: Meta no lo admite.

Por eso el botón **Authenticate** no se puede usar. El endpoint está activo, pero actualmente exige un cliente OAuth previamente registrado.

La solución es crear/usar una aplicación en **Meta for Developers**, obtener su **App ID** y volver a configurarlo:

```bash
codex mcp remove facebook-ads

codex mcp add facebook-ads \
  --url https://mcp.facebook.com/ads \
  --oauth-client-id TU_META_APP_ID
```

Codex mostrará una **OAuth callback URL**. Tenés que copiar exactamente esa URL en la configuración de OAuth de tu aplicación de Meta como redirect URI. Después ejecutás:

```bash
codex mcp login facebook-ads
```

No compartas el **App Secret**; para configurarlo solamente hace falta el **App ID**. Si no tenés una aplicación de Meta registrada, el MCP no se puede autenticar automáticamente hasta que Meta corrija o habilite su registro dinámico para Codex. Este flujo con Client ID pre-registrado está contemplado por la [documentación oficial de MCP en Codex](https://developers.openai.com/codex/mcp/).
