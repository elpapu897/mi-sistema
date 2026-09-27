# Carrusel "Chau Pelos" — GONVRA

**Producto:** Combo Chau Pelos — Cepillo a Vapor 3en1 + Guante Removedor · **$20.990**
**Link:** gonvra.com/products/combo-chau-pelos
**Formato:** 4:5 vertical, 2K (subir directo a Instagram/TikTok)

---

## ✅ Versión FINAL — texto ya incluido en la imagen

Estos son los que se publican. No necesitan Canva.

| # | Archivo | Texto que trae |
|---|---------|----------------|
| 1 | `estilo-test.png` | CHAU **PELOS** EN TU CASA · "Cepillo a vapor + guante removedor" · botón DESLIZA |
| 2 | `slide2-txt.png` | TU SILLÓN. TU ROPA. **TU PACIENCIA.** · "Todo con pelos. Todos los días." |
| 3 | `slide3-txt.png` | SACÁ EL PELO **ANTES DE QUE SE CAIGA** · "El cepillo a vapor lo junta directo del animal." |
| 4 | `slide4-txt.png` | JUNTÁ EL QUE **YA QUEDÓ EN CASA** · "Sillón, ropa y alfombras en una pasada." |
| 5 | `slide5-txt.png` | EL MISMO SILLÓN. **30 SEGUNDOS DESPUÉS.** · ANTES/DESPUÉS · "Sin aspiradora, sin cinta, sin renegar." |
| 6 | `slide6-txt.png` | COMBO **CHAU PELOS** · **$20.990** · botón LINK EN LA BIO |

**Estilo:** azul noche `#0A1628` + ámbar `#E8A33D`, Montserrat ExtraBold mayúsculas,
bicolor blanco/ámbar, numeración 01-06 en cuadrito, reglas finas ámbar.
Basado en las referencias de carrusel de agencia (Burger House / Sonríe).

---

## Versión limpia (sin texto) — de respaldo

Por si querés maquetar vos en Canva: `slide1.png` … `slide6.png`.
Mismas fotos pero sin nada encima.

**Bonus para otro carrusel:** `bonus-meme.png` (perro + montaña de pelo)
> Texto sugerido: *"Mi perro cuando ve que saqué el cepillo nuevo:"*

---

## ⚠️ Correcciones sobre la ficha original

1. **El guante NO es de silicona.** Es una manopla de tela negra con etiqueta
   blanca y naranja. Las imágenes usan la foto real de la tienda.
2. En la tienda el producto es **"Chau Pelos"**, no "Chao Pelos".

---

## Cómo regenerar un slide

```bash
python ~/Claude/scripts/genimage-replicate.py \
  --model nano-banana-pro --aspect-ratio 4:5 --resolution 2K \
  --images ref/cepillo.png \
  --prompt "..." --output slideX-txt.png
```

### Reglas que funcionaron

- **nano-banana-pro escribe bien en español**, con acentos incluidos
  (SILLÓN, DESPUÉS, SACÁ, días). Los modelos más baratos no.
- Cerrar el prompt con: `"Render all Spanish text with perfect spelling exactly
  as written including accents. No gibberish, no misspellings, no watermark."`
- **El guante recortado se lee como pantufla.** Si pasás `ref/guante.png` directo,
  el modelo dibuja un chancleta. La solución que funcionó: generar primero la
  foto limpia con `nano-banana` y después pasarle **esa foto** a `nano-banana-pro`
  pidiéndole que la use tal cual y le agregue el diseño encima.

### Referencias de producto

- `ref/cepillo.png` — cepillo dorado, cerdas naranjas (funciona directo)
- `ref/guante.png` — manopla negra (mejor usar `slide4.png` ya generada)
- `ref/ref1.png`, `ref2.jpg`, `ref3.png` — fotos originales de la tienda
