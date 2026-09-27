---
tool: Codex
session_id: 01a0b2a2-ae0a-73c1-b781-84c4b1b6a165
fecha: 2026-09-18 03:50
titulo: "Sino que me digas qué IA local me recomendás para"
tags: [chat, agente, codex]
---

# 💬 Sino que me digas qué IA local me recomendás para
> **Codex** · 2026-09-18 03:50 · `01a0b2a2-ae0a-73c1-b781-84c4b1b6a165`

---

### 🧑 Vos  <small>2026-09-18 03:50</small>

Sino que me digas qué IA local me recomendás para mi PC, por favor.

### 🤖 Codex  <small>2026-09-18 03:50</small>

Voy a mirar CPU, RAM, GPU y sistema operativo de tu PC, y con eso te recomiendo modelos locales concretos y qué programa usar para correrlos. Después contrasto con las opciones actuales.

### 🤖 Codex  <small>2026-09-18 03:50</small>

Ya veo el límite importante: tenés un Ryzen 5 7430U, 16 GB de RAM y gráfica AMD integrada, sin VRAM dedicada. Eso favorece modelos chicos/medianos cuantizados; voy a revisar qué aceleración está disponible y si ya tenés algún runtime instalado.

### 🤖 Codex  <small>2026-09-18 03:51</small>

Para tu PC, si buscás un asistente tipo ChatGPT local, mi recomendación concreta es:

**Qwen 3.5 4B + Ollama + Alpaca**

Tu equipo tiene Ryzen 5 7430U, 16 GB de RAM y gráfica AMD integrada. Qwen 3.5 4B cuantizado ocupa unos **3,4 GB**, entiende bien español, programa razonablemente y ofrece una buena relación entre calidad y velocidad. [Ficha del modelo](https://ollama.com/library/qwen3.5).

Configuración aconsejada:

- Modelo principal: `qwen3.5:4b`
- Contexto: 4.096 tokens; como máximo 8.192
- Interfaz gráfica: [Alpaca](https://flathub.org/apps/com.jeffser.Alpaca), especialmente cómoda en Fedora
- Motor: [Ollama](https://docs.ollama.com/linux)
- Para mayor velocidad: `qwen3.5:2b`
- Para mayor calidad, aceptando bastante lentitud: `qwen3.5:9b`
- Evitaría modelos de 14B o más en esta máquina.

Tu gráfica Barcelo no aparece entre las AMD oficialmente soportadas mediante ROCm. Probaría la aceleración Vulkan de Ollama y dejaría CPU como alternativa; Ollama ofrece ambas posibilidades en Linux. [Compatibilidad de hardware](https://docs.ollama.com/gpu).

Un detalle: ahora mismo tenés 11 GB de RAM ocupados y 4,4 GB de swap utilizados. Conviene cerrar navegador y aplicaciones pesadas antes de cargar el modelo. Aunque Qwen anuncie 256K de contexto, en tu PC eso no es práctico porque el contexto aumenta mucho el consumo de memoria. [Explicación de contexto](https://docs.ollama.com/context-length).

**Resumen:** empezaría con **Qwen 3.5 4B**. Es el punto justo para tu hardware. Si querés, también puedo instalarlo y dejarte Alpaca configurado.

### 🧑 Vos  <small>2026-09-18 03:53</small>

kmi k3?

### 🤖 Codex  <small>2026-09-18 03:53</small>

¿Te referís a **Kimi K3**? Voy a comprobar qué versiones locales existen y si alguna entra razonablemente en tus 16 GB de RAM.

### 🤖 Codex  <small>2026-09-18 03:53</small>

Ah, **Kimi K3**. Es excelente, pero **no es viable localmente en tu PC**.

Tiene **2,8 billones de parámetros totales** y 104B activos. Incluso cuantizado a 4 bits necesitaría teóricamente alrededor de **1,4 TB solamente para los pesos**, frente a tus 16 GB de RAM. [Ficha oficial de Kimi K3](https://huggingface.co/moonshotai/Kimi-K3).

Podés usarlo mediante la web o API de Kimi, pero no ejecutarlo realmente en tu notebook. Los modelos de Ollama llamados `kimi-k3` no hacen que mágicamente entre: suelen ser conexiones remotas, conversiones incompletas o experimentos inviables para hardware normal.

Para uso verdaderamente local sigo recomendándote:

- **Qwen 3.5 4B:** opción equilibrada.
- **Qwen 3.5 2B:** más rápido.
- **Qwen 3.5 9B:** mejor, pero bastante más lento y exige cerrar otras aplicaciones.

En resumen: **Kimi K3 en la nube; Qwen 3.5 4B local.**

### 🧑 Vos  <small>2026-09-18 03:54</small>

Bueno, quiero que mejores todo mi PC, por así decirlo. quiero que elimines todo lo que no estoy utilizando, todo para trabajar. Solo los dos juegos que tengo, que es el Minecraft y el Roblox, dejalos, pero después todo elimínalo, no sé, límpialo para tener, para que utilice 10 menos RAM y todo eso. por favor, elimíname todo.

### 🤖 Codex  <small>2026-09-18 03:55</small>

Voy a hacer primero una auditoría completa y separar tres cosas: procesos que consumen RAM, programas instalados y archivos que ocupan disco. Voy a preservar Minecraft, Roblox, tus documentos y proyectos; antes de cualquier borrado material te mostraré objetivos concretos, porque “lo que no uso” no se puede deducir con seguridad sólo por estar instalado.

### 🤖 Codex  <small>2026-09-18 03:55</small>

Encontré el problema principal: no es que Fedora “use 10 GB sola”. Tenés abiertos al mismo tiempo Brave con muchos procesos, Codex, Claude, Hermes, OpenCode y Antigravity; además Hermes arranca automáticamente. Varias son aplicaciones Electron y juntas explican casi toda la presión de RAM y los 6,3 GB de swap. Sigo relevando cuánto consume cada grupo y cuáles arrancan solas.

### 🤖 Codex  <small>2026-09-18 03:56</small>

Ya está claro que borrar aplicaciones instaladas por sí solo no bajará 10 GB de RAM: el ahorro real viene de no mantener seis entornos pesados abiertos a la vez. También encontré **51 GB de caché**, **26 GB en Descargas** y **22 GB bajo configuraciones**, así que voy a identificar exactamente qué hay ahí sin tocar Minecraft, Sober/Roblox, proyectos ni documentos.

### 🤖 Codex  <small>2026-09-18 03:57</small>

Hay dos limpiezas inequívocas y seguras: el actualizador de Codex acumuló unas **23 versiones extraídas antiguas (≈40 GB)**, y Descargas contiene **cuatro copias del instalador de DaVinci Resolve (≈15,6 GB)** aunque Resolve ya está instalado. Voy a validar esas copias y conservar tanto la versión de Codex instalada como la actualización pendiente.

### 🤖 Codex  <small>2026-09-18 03:58</small>

El sistema bloqueó el borrado permanente directo, así que voy a usar la Papelera, que es recuperable. No se tocó nada con el intento anterior. Moveré únicamente las versiones antiguas verificadas y los instaladores duplicados; después revisaré el resultado antes de vaciar nada.
