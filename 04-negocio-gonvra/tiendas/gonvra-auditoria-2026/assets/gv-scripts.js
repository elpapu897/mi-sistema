/* GONVRA — interacciones propias. Todo vanilla, sin librerías. */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Solo ocultamos contenido para animarlo si el JS realmente está corriendo.
     Si este archivo no carga o falla, nada queda invisible. */
  document.documentElement.classList.add('gv-js');

  /* iOS/Android: un listener táctil vacío habilita los estilos :active
     (el "movimiento al tocar" de tarjetas y opiniones). */
  if (!window.__gvTouch) {
    window.__gvTouch = true;
    document.addEventListener('touchstart', function () {}, { passive: true });
  }

  /* Red de seguridad: pase lo que pase, a los 2,5 s todo bloque pendiente queda
     en su posición final. Ninguna sección puede quedar descolocada ni oculta. */
  window.setTimeout(function () {
    var pendientes = document.querySelectorAll('.gv-reveal:not(.gv-visible)');
    for (var i = 0; i < pendientes.length; i++) pendientes[i].classList.add('gv-visible');
  }, 2500);

  /* Marca un elemento como inicializado POR MÓDULO. Evita listeners duplicados
     cuando el editor de Shopify redibuja una sección, sin que un módulo "pise" a
     otro: un mismo nodo puede ser a la vez .gv-reveal y [data-gv-acc]. */
  function nuevo(el, modulo) {
    if (!el) return false;
    if (!el.__gv) el.__gv = {};
    if (el.__gv[modulo]) return false;
    el.__gv[modulo] = true;
    return true;
  }
  /* Devuelve un filtro listo para usar con .filter(...) sin que el índice
     del array se cuele como nombre de módulo. */
  function soloNuevos(modulo) {
    return function (el) { return nuevo(el, modulo); };
  }

  /* --- Reveal al hacer scroll --- */
  function initReveals() {
    var els = [].slice.call(document.querySelectorAll('.gv-reveal')).filter(soloNuevos('reveal'));
    if (!els.length) return;
    if (reduced || !('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('gv-visible'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('gv-visible');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  /* --- Galería de la página de producto --- */
  function initGallery() {
    var gallery = document.querySelector('[data-gv-gallery]');
    if (!gallery || !nuevo(gallery, 'galeria')) return;
    var main = gallery.querySelector('[data-gv-main-img]');
    var thumbs = gallery.querySelectorAll('[data-gv-thumb]');
    if (!main || !thumbs.length) return;
    thumbs.forEach(function (t) {
      t.addEventListener('click', function () {
        var full = t.getAttribute('data-full');
        if (full) main.src = full;
        thumbs.forEach(function (x) { x.classList.remove('is-active'); });
        t.classList.add('is-active');
      });
    });
  }

  /* --- Selector de variantes + ofertas por cantidad --- */
  function initVariants() {
    var root = document.querySelector('[data-gv-product]');
    if (!root || !nuevo(root, 'variantes')) return;
    var dataEl = root.querySelector('[data-gv-variants-json]');
    if (!dataEl) return;
    var variants;
    try { variants = JSON.parse(dataEl.textContent); } catch (e) { return; }

    var idInput = root.querySelector('[data-gv-variant-id]');
    var priceNow = root.querySelector('[data-gv-price-now]');
    var priceWas = root.querySelector('[data-gv-price-was]');
    var priceSave = root.querySelector('[data-gv-price-save]');
    var addBtn = root.querySelector('[data-gv-add]');
    var qtyInput = root.querySelector('[data-gv-quantity]');
    var addLabel = addBtn ? addBtn.getAttribute('data-label') : 'Agregar al carrito';
    var soldLabel = addBtn ? addBtn.getAttribute('data-sold') : 'Agotado';
    var moneyFmt = root.getAttribute('data-money') || '${{amount}}';
    var offers = Array.prototype.slice.call(root.querySelectorAll('[data-gv-offer]'));
    var currentUnit = variants[0] ? variants[0].price : 0;
    var stickyPrice = root.querySelector('[data-gv-sticky-price]');
    var stickyWas = root.querySelector('[data-gv-sticky-was]');
    var stickyBtn = root.querySelector('[data-gv-sticky-btn]');
    var form = root.querySelector('form[action*="/cart/add"]');

    function formatMoney(cents) {
      var amount = cents / 100;
      return moneyFmt.replace(/\{\{\s*(\w+)\s*\}\}/g, function (_, name) {
        var decimals = name.indexOf('no_decimals') !== -1 ? 0 : 2;
        var locale = 'en-US';
        if (name.indexOf('comma_separator') !== -1) locale = 'es-AR';
        else if (name.indexOf('space_separator') !== -1) locale = 'fr-FR';
        return amount.toLocaleString(locale, { minimumFractionDigits: decimals, maximumFractionDigits: decimals });
      });
    }

    function currentSelection() {
      var sel = [];
      root.querySelectorAll('[data-gv-option-index]').forEach(function (group) {
        var idx = parseInt(group.getAttribute('data-gv-option-index'), 10);
        var active = group.querySelector('[data-value].is-active');
        sel[idx] = active ? active.getAttribute('data-value') : null;
        var label = group.querySelector('[data-gv-selected-' + idx + ']');
        if (label && active) label.textContent = active.getAttribute('data-value');
      });
      return sel;
    }

    function updateOffers() {
      offers.forEach(function (off) {
        var qty = parseInt(off.getAttribute('data-qty'), 10) || 1;
        var disc = parseInt(off.getAttribute('data-off'), 10) || 0;
        var discUnits = qty - 1; /* solo las unidades extra llevan descuento */
        var was = currentUnit * qty;
        var now = Math.round(was - currentUnit * (disc / 100) * discUnits);
        var save = was - now;
        var nowEl = off.querySelector('[data-gv-offer-now]');
        var wasEl = off.querySelector('[data-gv-offer-was]');
        var subEl = off.querySelector('[data-gv-offer-sub]');
        var unitEl = off.querySelector('[data-gv-offer-unit]');
        if (nowEl) nowEl.textContent = formatMoney(now);
        if (wasEl) {
          if (disc > 0) { wasEl.textContent = formatMoney(was); wasEl.style.display = ''; }
          else { wasEl.style.display = 'none'; }
        }
        if (subEl && disc > 0) subEl.textContent = 'Ahorrás ' + formatMoney(save);
        if (unitEl) {
          if (qty > 1) { unitEl.textContent = formatMoney(Math.round(now / qty)) + ' c/u'; unitEl.style.display = ''; }
          else { unitEl.style.display = 'none'; }
        }
      });
    }

    function selectOffer(off) {
      offers.forEach(function (o) {
        o.classList.remove('is-active');
        var r = o.querySelector('input[type=radio]');
        if (r) r.checked = false;
      });
      off.classList.add('is-active');
      var r = off.querySelector('input[type=radio]');
      if (r) r.checked = true;
      if (qtyInput) qtyInput.value = off.getAttribute('data-qty');
    }

    function update() {
      var sel = currentSelection();
      var match = variants.find(function (v) {
        return v.options.every(function (opt, i) { return opt === sel[i]; });
      });
      if (!match) match = variants[0]; /* fallback: productos de una sola variante (Default Title) */
      if (!match) return;
      currentUnit = match.price;
      if (idInput) idInput.value = match.id;
      if (priceNow) priceNow.textContent = formatMoney(match.price);
      if (priceWas) {
        if (match.compare_at_price && match.compare_at_price > match.price) {
          priceWas.textContent = formatMoney(match.compare_at_price);
          priceWas.style.display = '';
          if (priceSave) {
            var pct = Math.round((1 - match.price / match.compare_at_price) * 100);
            priceSave.textContent = '-' + pct + '%';
            priceSave.style.display = '';
          }
        } else {
          priceWas.style.display = 'none';
          if (priceSave) priceSave.style.display = 'none';
        }
      }
      if (addBtn) {
        if (match.available) { addBtn.disabled = false; addBtn.textContent = addLabel; }
        else { addBtn.disabled = true; addBtn.textContent = soldLabel; }
      }
      if (stickyPrice) stickyPrice.textContent = formatMoney(match.price);
      if (stickyWas) {
        if (match.compare_at_price && match.compare_at_price > match.price) {
          stickyWas.textContent = formatMoney(match.compare_at_price);
          stickyWas.style.display = '';
        } else { stickyWas.style.display = 'none'; }
      }
      if (stickyBtn) stickyBtn.disabled = !match.available;
      updateOffers();
    }

    if (stickyBtn && form) {
      stickyBtn.addEventListener('click', function () {
        if (form.requestSubmit) form.requestSubmit();
        else form.submit();
      });
    }

    root.querySelectorAll('[data-gv-option-index]').forEach(function (group) {
      group.querySelectorAll('[data-value]').forEach(function (sw) {
        sw.addEventListener('click', function () {
          group.querySelectorAll('[data-value]').forEach(function (x) { x.classList.remove('is-active'); });
          sw.classList.add('is-active');
          update();
        });
      });
    });

    offers.forEach(function (off) {
      off.addEventListener('click', function () { selectOffer(off); });
    });

    update();
  }

  /* --- Cantidad --- */
  function initQty() {
    [].slice.call(document.querySelectorAll('[data-gv-qty]')).filter(soloNuevos('qty')).forEach(function (wrap) {
      var input = wrap.querySelector('input');
      if (!input) return;
      wrap.querySelectorAll('button').forEach(function (b) {
        b.addEventListener('click', function () {
          var step = b.getAttribute('data-step') === 'up' ? 1 : -1;
          var val = parseInt(input.value, 10) || 1;
          val = Math.max(1, val + step);
          input.value = val;
        });
      });
    });
  }

  /* --- Mostrar la barra fija al pasar el botón de compra --- */
  function initSticky() {
    var bar = document.querySelector('[data-gv-sticky]');
    var anchor = document.querySelector('[data-gv-add]');
    if (!bar || !anchor || !nuevo(bar, 'sticky')) return;
    if (!('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        /* visible cuando el botón principal ya quedó arriba de la pantalla */
        if (!e.isIntersecting && e.boundingClientRect.top < 0) bar.classList.add('is-visible');
        else bar.classList.remove('is-visible');
      });
    }, { threshold: 0 });
    io.observe(anchor);
  }

  /* --- Acordeón --- */
  function initAcordeon() {
    var lists = [].slice.call(document.querySelectorAll('[data-gv-acc]')).filter(soloNuevos('acordeon'));
    if (!lists.length) return;
    lists.forEach(function (list) {
      var items = [].slice.call(list.querySelectorAll('.gv-acc__item'));
      items.forEach(function (item) {
        var head = item.querySelector('[data-gv-acc-head]');
        var panel = item.querySelector('[data-gv-acc-panel]');
        if (!head || !panel) return;

        function abrir() {
          panel.style.height = panel.scrollHeight + 'px';
          item.classList.add('is-open');
          head.setAttribute('aria-expanded', 'true');
          window.setTimeout(function () {
            if (item.classList.contains('is-open')) panel.style.height = 'auto';
          }, 400);
        }
        function cerrar() {
          panel.style.height = panel.scrollHeight + 'px';
          window.requestAnimationFrame(function () {
            panel.style.height = '0px';
          });
          item.classList.remove('is-open');
          head.setAttribute('aria-expanded', 'false');
        }

        if (item.classList.contains('is-open')) panel.style.height = 'auto';

        head.addEventListener('click', function () {
          var abierto = item.classList.contains('is-open');
          /* solo uno abierto a la vez */
          items.forEach(function (otro) {
            if (otro !== item && otro.classList.contains('is-open')) {
              var p = otro.querySelector('[data-gv-acc-panel]');
              var h = otro.querySelector('[data-gv-acc-head]');
              if (p) {
                p.style.height = p.scrollHeight + 'px';
                window.requestAnimationFrame(function () { p.style.height = '0px'; });
              }
              otro.classList.remove('is-open');
              if (h) h.setAttribute('aria-expanded', 'false');
            }
          });
          if (abierto) cerrar(); else abrir();
        });
      });
    });
  }

  /* --- Videos: reproducir en silencio al entrar en pantalla --- */
  function initVideos() {
    /* El <video> lo genera Shopify dentro de .gv-vid__media, así que lo buscamos por el DOM */
    var vids = [].slice.call(document.querySelectorAll('.gv-vid video')).filter(soloNuevos('video'));
    if (vids.length && 'IntersectionObserver' in window && !reduced) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          var v = e.target;
          try {
            if (e.isIntersecting) { v.muted = true; var p = v.play(); if (p && p.catch) p.catch(function () {}); }
            else { v.pause(); }
          } catch (err) { /* un video roto no debe romper la página */ }
        });
      }, { threshold: 0.35 });
      vids.forEach(function (v) { v.muted = true; io.observe(v); });
    }

    [].slice.call(document.querySelectorAll('[data-gv-vid-sound]')).filter(soloNuevos('sonido')).forEach(function (btn) {
      btn.addEventListener('click', function () {
        var card = btn.closest('.gv-vid');
        var v = card ? card.querySelector('video') : null;
        if (!v) return;
        v.muted = !v.muted;
        if (!v.muted) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
        btn.style.background = v.muted ? '' : 'var(--gv-aqua)';
      });
    });

    /* YouTube / Vimeo: se cargan solo al hacer clic */
    [].slice.call(document.querySelectorAll('[data-gv-vid-embed]')).filter(soloNuevos('embed')).forEach(function (btn) {
      btn.addEventListener('click', function () {
        var card = btn.closest('.gv-vid');
        var src = btn.getAttribute('data-src');
        if (!card || !src) return;
        var f = document.createElement('iframe');
        f.setAttribute('src', src);
        f.setAttribute('allow', 'autoplay; encrypted-media; picture-in-picture');
        f.setAttribute('allowfullscreen', '');
        f.setAttribute('title', 'Video del producto');
        card.appendChild(f);
        btn.remove();
        var cover = card.querySelector('[data-gv-vid-cover]');
        if (cover) cover.style.display = 'none';
      });
    });
  }

  /* --- Carruseles móviles (beneficios, favoritos, reseñas, sellos, características) ---
     El contenedor sigue siendo una grilla normal en escritorio; el CSS lo vuelve
     fila deslizable solo en pantallas chicas. Acá solo agregamos auto-avance y
     flechas. Si nada desborda (escritorio), el avance no hace nada. */
  function initCarruseles() {
    var carrs = [].slice.call(document.querySelectorAll('[data-gv-carousel]')).filter(soloNuevos('carrusel'));
    carrs.forEach(function (carr) {
      var auto = parseInt(carr.getAttribute('data-auto') || '0', 10);
      var timer = null;

      function activo() { return carr.scrollWidth - carr.clientWidth > 20; }
      function paso(dir) {
        if (!activo()) return;
        var hijos = carr.children;
        if (!hijos.length) return;
        var ancho = hijos.length > 1
          ? hijos[1].offsetLeft - hijos[0].offsetLeft
          : hijos[0].getBoundingClientRect().width;
        if (ancho <= 0) return;
        var max = carr.scrollWidth - carr.clientWidth;
        var destino = carr.scrollLeft + dir * ancho;
        if (dir > 0 && carr.scrollLeft >= max - 10) destino = 0;
        if (dir < 0 && carr.scrollLeft <= 10) destino = max;
        if (destino > max) destino = max;
        if (destino < 0) destino = 0;
        carr.scrollTo({ left: destino, behavior: reduced ? 'auto' : 'smooth' });
      }
      function detener() { if (timer) { clearInterval(timer); timer = null; } }

      if (carr.hasAttribute('data-arrows')) {
        var padre = carr.parentNode;
        if (padre && getComputedStyle(padre).position === 'static') padre.style.position = 'relative';
        var colocar = function (btn) {
          btn.style.top = (carr.offsetTop + carr.offsetHeight / 2) + 'px';
        };
        [['prev', -1], ['next', 1]].forEach(function (par) {
          var b = document.createElement('button');
          b.type = 'button';
          b.className = 'gv-carr-arrow gv-carr-arrow--' + par[0];
          b.setAttribute('aria-label', par[0] === 'prev' ? 'Ver anterior' : 'Ver siguiente');
          b.innerHTML = par[1] < 0
            ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>'
            : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>';
          b.addEventListener('click', function () { detener(); paso(par[1]); });
          padre.appendChild(b);
          colocar(b);
          window.addEventListener('resize', function () { colocar(b); });
          window.addEventListener('load', function () { colocar(b); });
        });
      }

      if (auto && !reduced) {
        ['pointerdown', 'touchstart'].forEach(function (ev) {
          carr.addEventListener(ev, detener, { passive: true });
        });
        timer = setInterval(function () { paso(1); }, auto);
      }
    });
  }

  /* Cada init va aislado: si uno falla, los demás siguen funcionando y la
     sección nunca queda en blanco. */
  function seguro(nombre, fn) {
    try { fn(); }
    catch (err) {
      if (window.console && console.warn) console.warn('[GONVRA] ' + nombre + ':', err);
    }
  }

  function boot() {
    seguro('reveals', initReveals);
    seguro('galeria', initGallery);
    seguro('variantes', initVariants);
    seguro('cantidad', initQty);
    seguro('barra-fija', initSticky);
    seguro('acordeon', initAcordeon);
    seguro('videos', initVideos);
    seguro('carruseles', initCarruseles);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

  /* El editor de Shopify redibuja secciones sin recargar la página:
     hay que volver a enganchar el JS o la sección queda "muerta"/en blanco. */
  document.addEventListener('shopify:section:load', boot);
  document.addEventListener('shopify:section:select', boot);
  document.addEventListener('shopify:block:select', boot);
})();
