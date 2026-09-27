# Plan de Auditoría y Corrección de Tema (GONVRA - Auditoría 2026)

Este plan detalla los cambios técnicos que realizaré en la copia local del tema para solucionar los problemas de confianza, coherencia y medición detectados en la auditoría, sin afectar la tienda en vivo.

> [!IMPORTANT]  
> **Aviso sobre Políticas y Panel de Shopify**  
> Las páginas de políticas (Envíos, Devoluciones con el marcador `[INSERTAR DIRECCIÓN DE DEVOLUCIÓN]`) se configuran desde el panel de control de Shopify (Configuración > Políticas), **no desde los ficheros del tema**. Te recordaré realizar esos cambios en el panel, mientras yo me encargo de corregir todas las menciones y enlaces en el código del tema.

## User Review Required

- **Sistema de reseñas**: La auditoría encontró Loox, Judge.me y testimonios en la portada. Voy a proceder a eliminar los rastros de **Loox** de los templates JSON y snippets del tema para unificar en un solo sistema.
- **Píxel de Facebook**: Eliminaré el bloque de la app *Parkour* de la configuración del tema (`settings_data.json`) para evitar eventos duplicados. Solo debería quedar el píxel oficial configurado por el canal de Meta en Shopify.
- **Correo y Redes**: Cambiaré `gonvra0@gmail.com` por un correo genérico bajo dominio propio (ej. `contacto@gonvra.com`) para aumentar la confianza. Deberás crear este correo.

## Proposed Changes

---

### Configuración del Tema y Analítica

#### [MODIFY] settings_data.json
- Eliminar el bloque de la aplicación *Parkour Facebook Pixel* que está inyectando un píxel adicional y duplicando el seguimiento.

---

### Fichas de Producto y Portada

#### [MODIFY] sections/gv-producto.liquid
- Revisar la lógica de selección de cantidad ("Llevá 2 unidades") para que por defecto se seleccione **solo 1 unidad**. El pack debe ser un *upsell* opcional, no una trampa preseleccionada para el tráfico frío.
- Limpiar menciones de "aggregateRating" forzados en el código.

#### [MODIFY] templates/product*.json
- **Limpieza de "Loox"**: Eliminar los bloques `loox_rating` y `loox_reviews` de las plantillas de producto para evitar fragmentación.
- **Eliminar exageraciones y contradicciones**: Limpiar reclamos engañosos ("Garantía 7 días" vs 10 días, "ortopédico", "antiestrés") en los textos de los bloques del producto principal.

#### [MODIFY] templates/index.json
- Cambiar el enlace de contacto temporal de `gonvra0@gmail.com` a `contacto@gonvra.com`.
- Revisar los testimonios estáticos para asegurar coherencia con el sistema de reseñas elegido.

---

### Snippets

#### [MODIFY] snippets/card-product.liquid
- Eliminar el div `loox-rating` inyectado en las tarjetas de colección para dejar de mostrar estrellas sin reseñas reales verificables.

## Verification Plan

### Manual Verification
- Visualizar el tema modificado usando `shopify theme dev` (o subiéndolo como tema no publicado).
- Verificar que la ficha de producto de la cama selecciona 1 unidad por defecto.
- Confirmar la desaparición de las estrellas vacías de Loox y que no se dispare un segundo píxel.
