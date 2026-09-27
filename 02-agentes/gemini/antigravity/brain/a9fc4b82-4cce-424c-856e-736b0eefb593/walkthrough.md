# Resumen de Auditoría y Correcciones Técnicas

Las tareas de corrección han sido implementadas exitosamente en la copia local del tema `GONVRA - Auditoría 2026`. 

## Cambios Realizados

- **Píxel de Facebook unificado**: Se ha eliminado el código inyectado por la aplicación *Parkour* de `config/settings_data.json`. Ahora solo debería registrar los eventos tu Píxel oficial configurado mediante el canal de Meta de Shopify, previniendo eventos duplicados o cruzados.
- **Transparencia en la Ficha de Producto**: 
  - La cantidad por defecto se ha establecido en **1 unidad**. La oferta de "Llevá 2 unidades" sigue disponible, pero ahora requiere una acción consciente por parte del usuario.
  - Se eliminaron las afirmaciones contradictorias sobre la duración de la garantía, estandarizando todo en **Garantía de 10 días** para que coincida con el título del producto y la portada de la tienda.
  - Se suavizaron las afirmaciones médicas injustificadas como "ortopédico" o "cuida las articulaciones" por descripciones más enfocadas en los beneficios reales: *Soporte completo*, *Diseño anatómico* y *Comodidad para el día a día*.
- **Confianza**: Se eliminaron los bloques inyectados de *Loox Reviews* que dejaban marcadores de estrellas vacías y fragmentaban tu prueba social.
- **Contacto**: Se reemplazó el correo temporal `gonvra0@gmail.com` por el correo profesional `contacto@gonvra.com` en toda la página de inicio.

> [!WARNING]
> **Acciones Pendientes en Shopify Admin**
> 
> Aunque el tema ahora está limpio y preparado, todavía debes realizar algunas correcciones desde el **panel de administración de Shopify**:
> 1. Ve a **Configuración > Políticas**.
> 2. Revisa la *Política de Envíos* (actualmente devuelve un error 404 en la tienda).
> 3. En la *Política de Devoluciones*, asegúrate de borrar el texto literal `[INSERTAR DIRECCIÓN DE DEVOLUCIÓN]` y verifica que el plazo indique 10 días, coincidiendo con lo prometido en la web.

> [!TIP]
> **Imágenes y Redes Sociales**
> Para aumentar aún más la conversión, recuerda reemplazar las fotos de producto que parecen sacadas de catálogo por fotos reales (si las tienes) y añadir los enlaces correctos a tu WhatsApp e Instagram en las opciones de personalización del tema.

## Próximos Pasos

Para verificar estos cambios, puedes abrir una previsualización de este tema mediante la herramienta de desarrollo de Shopify CLI:
```bash
shopify theme dev --store=9em58g-tt.myshopify.com
```

O si prefieres, podemos subir este tema al panel como un tema no publicado usando el comando `shopify theme push`. ¡Avísame cómo prefieres continuar!
