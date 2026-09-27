/* ==========================================================================
   MT PLUS — comportamiento de las secciones añadidas
   Sin dependencias. Respeta prefers-reduced-motion.
   ========================================================================== */
(() => {
  'use strict';

  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------------------------------------------------------- reveal */
  function initReveal(root) {
    const items = root.querySelectorAll('.mtp-fade:not([data-mtp-ready]), .mtp-rule:not([data-mtp-ready]), .mtp-about__media:not([data-mtp-ready])');
    if (!items.length) return;
    items.forEach((el) => (el.dataset.mtpReady = 'true'));

    if (reduced || !('IntersectionObserver' in window)) {
      items.forEach((el) => el.classList.add('is-in'));
      return;
    }
    const io = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        obs.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });
    items.forEach((el) => io.observe(el));
  }

  /* ------------------------------------------------- titulares por palabra */
  function initSplit(root) {
    root.querySelectorAll('[data-mtp-split]:not([data-mtp-split-ready])').forEach((el) => {
      el.dataset.mtpSplitReady = 'true';
      if (reduced) { el.classList.add('is-in'); return; }
      const words = el.textContent.trim().split(/\s+/);
      el.textContent = '';
      words.forEach((word, i) => {
        const span = document.createElement('span');
        span.className = 'mtp-split';
        const inner = document.createElement('i');
        inner.textContent = word;
        inner.style.transitionDelay = `${i * 0.05}s`;
        span.appendChild(inner);
        el.appendChild(span);
        if (i < words.length - 1) el.appendChild(document.createTextNode(' '));
      });
      if ('IntersectionObserver' in window) {
        const io = new IntersectionObserver((entries, obs) => {
          entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add('is-in');
            obs.unobserve(entry.target);
          });
        }, { threshold: 0.25 });
        io.observe(el);
      } else {
        el.classList.add('is-in');
      }
    });
  }

  /* -------------------------------------------------------- halo de cursor */
  function initGlow(root) {
    root.querySelectorAll('.mtp-glow:not([data-mtp-glow-ready])').forEach((card) => {
      card.dataset.mtpGlowReady = 'true';
      card.addEventListener('pointermove', (event) => {
        const rect = card.getBoundingClientRect();
        card.style.setProperty('--mx', `${event.clientX - rect.left}px`);
        card.style.setProperty('--my', `${event.clientY - rect.top}px`);
      });
    });
  }

  /* ------------------------------------------------------------ contadores */
  function initCounters(root) {
    const counters = root.querySelectorAll('[data-mtp-count]:not([data-mtp-count-ready])');
    if (!counters.length) return;
    counters.forEach((el) => (el.dataset.mtpCountReady = 'true'));

    const run = (el) => {
      const target = parseFloat(el.dataset.mtpCount) || 0;
      const decimals = (el.dataset.mtpCount.split('.')[1] || '').length;
      if (reduced) { el.textContent = target.toFixed(decimals); return; }
      const duration = 1500;
      const start = performance.now();
      const tick = (now) => {
        const p = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = (target * eased).toFixed(decimals);
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };

    if (!('IntersectionObserver' in window)) { counters.forEach(run); return; }
    const io = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        run(entry.target);
        obs.unobserve(entry.target);
      });
    }, { threshold: 0.5 });
    counters.forEach((el) => io.observe(el));
  }

  /* ------------------------------------------------ ficha con puntos vivos */
  function initHotspots(root) {
    root.querySelectorAll('[data-mtp-hotspots]:not([data-mtp-hotspots-ready])').forEach((wrap) => {
      wrap.dataset.mtpHotspotsReady = 'true';
      const pins = Array.from(wrap.querySelectorAll('.mtp-hotspot__pin'));
      const specs = Array.from(wrap.querySelectorAll('.mtp-spec'));

      const activate = (key) => {
        pins.forEach((p) => p.classList.toggle('is-active', p.dataset.mtpKey === key));
        specs.forEach((s) => s.classList.toggle('is-active', s.dataset.mtpKey === key));
      };
      const clear = () => { pins.forEach((p) => p.classList.remove('is-active')); specs.forEach((s) => s.classList.remove('is-active')); };

      pins.forEach((pin) => {
        pin.addEventListener('mouseenter', () => activate(pin.dataset.mtpKey));
        pin.addEventListener('focus', () => activate(pin.dataset.mtpKey));
        pin.addEventListener('click', () => {
          activate(pin.dataset.mtpKey);
          const spec = specs.find((s) => s.dataset.mtpKey === pin.dataset.mtpKey);
          if (spec) spec.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'center' });
        });
      });
      specs.forEach((spec) => {
        spec.addEventListener('mouseenter', () => activate(spec.dataset.mtpKey));
        spec.addEventListener('mouseleave', clear);
      });
      wrap.addEventListener('mouseleave', clear);
    });
  }

  /* ----------------------------------------------------------------- video */
  function initVideo(root) {
    root.querySelectorAll('[data-mtp-video]:not([data-mtp-video-ready])').forEach((stage) => {
      stage.dataset.mtpVideoReady = 'true';
      const poster = stage.querySelector('.mtp-video__poster');
      if (!poster) return;
      poster.addEventListener('click', () => {
        const native = stage.querySelector('video');
        const embedUrl = stage.dataset.mtpEmbed;
        if (native) {
          native.play();
        } else if (embedUrl) {
          const frame = document.createElement('iframe');
          frame.src = embedUrl;
          frame.setAttribute('allow', 'autoplay; encrypted-media; picture-in-picture');
          frame.setAttribute('allowfullscreen', '');
          frame.setAttribute('title', stage.dataset.mtpTitle || 'Video');
          stage.appendChild(frame);
        }
        poster.classList.add('is-hidden');
      });
    });
  }

  /* -------------------------------------------------------------- carrusel */
  function initCarousel(root) {
    root.querySelectorAll('[data-mtp-carousel]:not([data-mtp-carousel-ready])').forEach((wrap) => {
      wrap.dataset.mtpCarouselReady = 'true';
      const viewport = wrap.querySelector('.mtp-carousel__viewport');
      const track = wrap.querySelector('.mtp-carousel__track');
      const prev = wrap.querySelector('[data-mtp-prev]');
      const next = wrap.querySelector('[data-mtp-next]');
      const bar = wrap.querySelector('.mtp-carousel__bar i');
      if (!viewport || !track) return;

      let offset = 0;
      const maxOffset = () => Math.max(0, track.scrollWidth - viewport.clientWidth);
      const step = () => {
        const slide = track.querySelector('.mtp-slide');
        if (!slide) return 320;
        const gap = parseFloat(getComputedStyle(track).columnGap || getComputedStyle(track).gap || 0) || 0;
        return slide.getBoundingClientRect().width + gap;
      };
      const apply = () => {
        offset = Math.min(Math.max(offset, 0), maxOffset());
        track.style.transform = `translate3d(${-offset}px, 0, 0)`;
        if (prev) prev.disabled = offset <= 1;
        if (next) next.disabled = offset >= maxOffset() - 1;
        if (bar) {
          const ratio = viewport.clientWidth / Math.max(track.scrollWidth, 1);
          const progress = maxOffset() ? offset / maxOffset() : 0;
          bar.style.width = `${Math.min(ratio * 100, 100)}%`;
          bar.style.transform = `translateX(${progress * (100 / Math.max(ratio, 0.01) - 100)}%)`;
        }
      };

      if (next) next.addEventListener('click', () => { offset += step(); apply(); });
      if (prev) prev.addEventListener('click', () => { offset -= step(); apply(); });

      /* arrastre con mouse / dedo */
      let startX = 0;
      let startOffset = 0;
      let dragging = false;
      viewport.addEventListener('pointerdown', (event) => {
        dragging = true;
        startX = event.clientX;
        startOffset = offset;
        track.classList.add('is-dragging');
        viewport.classList.add('is-dragging');
        viewport.setPointerCapture(event.pointerId);
      });
      viewport.addEventListener('pointermove', (event) => {
        if (!dragging) return;
        offset = startOffset - (event.clientX - startX);
        track.style.transform = `translate3d(${-Math.min(Math.max(offset, 0), maxOffset())}px, 0, 0)`;
      });
      const endDrag = () => {
        if (!dragging) return;
        dragging = false;
        track.classList.remove('is-dragging');
        viewport.classList.remove('is-dragging');
        apply();
      };
      viewport.addEventListener('pointerup', endDrag);
      viewport.addEventListener('pointercancel', endDrag);
      viewport.addEventListener('pointerleave', endDrag);

      window.addEventListener('resize', apply);
      apply();
    });
  }

  /* ------------------------------------------------------- barra de stock */
  function initStockBar(root) {
    root.querySelectorAll('.mtp-stockbar__fill:not([data-mtp-bar-ready])').forEach((fill) => {
      fill.dataset.mtpBarReady = 'true';
      const pct = Math.min(Math.max(parseFloat(fill.dataset.mtpPct) || 0, 4), 100);
      window.setTimeout(() => { fill.style.width = `${pct}%`; }, 250);
    });
  }

  /* -------------------------------------------------------------- arranque */
  function init(root = document) {
    initReveal(root);
    initSplit(root);
    initGlow(root);
    initCounters(root);
    initHotspots(root);
    initVideo(root);
    initCarousel(root);
    initStockBar(root);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => init());
  } else {
    init();
  }
  document.addEventListener('shopify:section:load', (event) => init(event.target));
})();
