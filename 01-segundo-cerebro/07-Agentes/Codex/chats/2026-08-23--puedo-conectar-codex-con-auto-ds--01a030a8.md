---
tool: Codex
session_id: 01a030a8-5d7a-7a83-a9b3-39a3c3563521
fecha: 2026-08-23 22:05
titulo: "puedo conectar codex con auto ds"
tags: [chat, agente, codex]
---

# 💬 puedo conectar codex con auto ds
> **Codex** · 2026-08-23 22:05 · `01a030a8-5d7a-7a83-a9b3-39a3c3563521`

---

### 🧑 Vos  <small>2026-08-23 22:05</small>

puedo conectar codex con auto ds

### 🤖 Codex  <small>2026-08-23 22:05</small>

Voy a comprobar qué opciones oficiales de integración ofrece AutoDS y si hay una conexión directa disponible desde Codex.

### 🤖 Codex  <small>2026-08-23 22:06</small>

Sí, pero hoy no hay un conector directo de AutoDS instalado en Codex.

La vía viable es integrar la API de AutoDS: permite importar productos, gestionar pedidos, sourcing y datos de catálogo. Requiere aprobación de AutoDS, un pago de activación y una suscripción activa. [Documentación oficial de AutoDS](https://help.autods.com/en/articles/12699964-autods-api-feature-automate-product-imports-orders-and-sourcing)

Podemos crear una integración propia para que Codex consulte productos, revise márgenes y prepare/importar borradores. Para publicar o procesar pedidos, conviene dejar confirmaciones explícitas antes de cada acción. AutoDS también tiene un conector MCP oficial, pero por ahora está documentado específicamente para Claude, no para Codex. [Conector MCP de AutoDS](https://help.autods.com/en/articles/15505185-autods-claude-mcp-connector-connect-claude-to-your-autods-account-search-products-and-manage-your-store)

### 🧑 Vos  <small>2026-08-23 22:06</small>

ok

### 🤖 Codex  <small>2026-08-23 22:06</small>

¿Querés que te guíe para solicitar acceso a la API de AutoDS y luego conectarla con Codex?

### 🧑 Vos  <small>2026-08-23 22:06</small>

si

### 🤖 Codex  <small>2026-08-23 22:06</small>

Te dejo el camino concreto: primero habilitamos la API en AutoDS y, cuando tengas las credenciales, armamos la conexión en este espacio.

### 🤖 Codex  <small>2026-08-23 22:07</small>

1. Pedí acceso desde la [página oficial de AutoDS API](https://www.autods.com/api/) o su [formulario de solicitud](https://help.autods.com/en/articles/12699964-autods-api-feature-automate-product-imports-orders-and-sourcing).

2. En “Describe your needs”, podés pegar esto:

   > I want to connect my AutoDS account to a private AI assistant workflow for product research, catalog analysis, margin reporting, draft product imports, and order-status monitoring. I need API documentation and credentials for my own store account.

3. AutoDS revisa el caso, informa el costo de activación y, si lo aprueba, entrega la documentación y credenciales. La API no tiene prueba gratuita y exige mantener una suscripción activa. [Detalles oficiales](https://help.autods.com/en/articles/12699964-autods-api-feature-automate-product-imports-orders-and-sourcing)

4. Cuando tengas acceso, no pegues tu clave/API token en el chat. Guardala localmente como variable de entorno o en un gestor de secretos. Decime qué método de autenticación indica la documentación y te preparo la integración.

Como primera versión, recomiendo habilitar solo lectura y creación de borradores; dejamos publicar productos y gestionar pedidos bajo confirmación explícita.
