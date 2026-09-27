
(() => {
  const root = document.querySelector('[data-gv]');
  if (!root) return;

  // Galería
  const track = root.querySelector('[data-gv-track]');
  const slides = track ? [...track.querySelectorAll('figure')] : [];
  const thumbs = [...root.querySelectorAll('[data-gv-thumb]')];
  const go = (i) => { if (slides[i]) track.scrollTo({ left: slides[i].offsetLeft, behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); };
  thumbs.forEach((t) => t.addEventListener('click', () => go(+t.dataset.gvThumb)));
  const prev = root.querySelector('[data-gv-prev]');
  const next = root.querySelector('[data-gv-next]');
  const current = () => Math.round(track.scrollLeft / Math.max(track.clientWidth, 1));
  if (prev) prev.addEventListener('click', () => go(Math.max(current() - 1, 0)));
  if (next) next.addEventListener('click', () => go(Math.min(current() + 1, slides.length - 1)));
  if (track) track.addEventListener('scroll', () => {
    const i = current();
    thumbs.forEach((t, k) => { t.classList.toggle('is-on', k === i); t.setAttribute('aria-selected', k === i ? 'true' : 'false'); });
  }, { passive: true });

  // Ofertas
  const qtyInput = root.querySelector('[data-gv-qty]');
  const total = root.querySelector('[data-gv-total]');
  const stickyTotal = root.querySelector('[data-gv-sticky-total]');
  const stickyQty = root.querySelector('[data-gv-sticky-qty]');
  const offers = [...root.querySelectorAll('[data-gv-offer]')];
  const pick = (btn) => {
    offers.forEach((o) => { o.classList.remove('is-on'); o.setAttribute('aria-checked', 'false'); });
    btn.classList.add('is-on');
    btn.setAttribute('aria-checked', 'true');
    if (qtyInput) qtyInput.value = btn.dataset.qty;
    if (total) total.textContent = btn.dataset.total;
    if (stickyTotal) stickyTotal.textContent = btn.dataset.total;
    if (stickyQty) stickyQty.textContent = btn.dataset.qty + (btn.dataset.qty === '1' ? ' unidad' : ' unidades');
  };
  offers.forEach((btn, index) => {
    btn.addEventListener('click', () => pick(btn));
    btn.addEventListener('keydown', event => {
      if (!['ArrowDown','ArrowUp','ArrowLeft','ArrowRight'].includes(event.key)) return;
      event.preventDefault();
      const direction = ['ArrowRight','ArrowDown'].includes(event.key) ? 1 : -1;
      const next = offers[(index + direction + offers.length) % offers.length];
      pick(next); next.focus();
    });
  });
  const preselected = offers.find((o) => o.classList.contains('is-on')) || offers[0];
  if (preselected) pick(preselected);

  // Si el pack elegido trae regalo, se agregan las dos cosas al carrito
  const form = root.querySelector('form[action*="/cart/add"]');
  if (form) {
    form.addEventListener('submit', (event) => {
      const active = root.querySelector('[data-gv-offer].is-on');
      const giftId = active && active.dataset.gift;
      if (!giftId) return;
      event.preventDefault();
      const variantId = form.querySelector('[name="id"]').value;
      const qty = parseInt(form.querySelector('[data-gv-qty]').value, 10) || 1;
      const button = form.querySelector('.gv-cta');
      if (button) { button.disabled = true; button.dataset.label = button.textContent; button.textContent = 'Agregando…'; }
      fetch('/cart/add.js', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ items: [{ id: Number(variantId), quantity: qty }, { id: Number(giftId), quantity: 1 }] })
      }).then((r) => r.json())
        .then(() => { window.location.href = '/cart'; })
        .catch(() => { form.submit(); });
    });
  }

  // Copiar código
  const code = root.querySelector('[data-gv-code]');
  if (code) code.addEventListener('click', () => {
    navigator.clipboard?.writeText(code.dataset.gvCode);
    const tag = code.querySelector('em');
    if (tag) { tag.textContent = 'copiado'; setTimeout(() => { tag.textContent = 'copiar'; }, 1800); }
  });

  // Contador hasta la hora de corte
  const clock = root.querySelector('[data-gv-clock]');
  if (clock) {
    const tick = () => {
      const cut = parseInt(clock.dataset.cutoff, 10) || 17;
      const now = new Date();
      const end = new Date(now);
      end.setHours(cut, 0, 0, 0);
      if (end <= now) end.setDate(end.getDate() + 1);
      const diff = end - now;
      const h = Math.floor(diff / 3600000);
      const m = Math.floor((diff % 3600000) / 60000);
      clock.textContent = h + ' h ' + String(m).padStart(2, '0') + ' min';
    };
    tick();
    setInterval(tick, 30000);
  }

  // Barra fija móvil
  const sticky = root.querySelector('[data-gv-sticky]');
  const cta = root.querySelector('.gv-cta');
  const addBtn = root.querySelector('[data-gv-sticky-add]');
  if (addBtn && form) addBtn.addEventListener('click', () => { if (cta && !cta.disabled) form.requestSubmit ? form.requestSubmit(cta) : form.submit(); });
  if (sticky && cta) {
    const watcher = new IntersectionObserver((e) => {
      e.forEach((entry) => {
        // sólo aparece cuando el botón ya quedó ARRIBA de la pantalla
        const passed = !entry.isIntersecting && entry.boundingClientRect.top < 0;
        sticky.classList.toggle('is-up', passed);
      });
    }, { threshold: 0 });
    watcher.observe(cta);
  }

  // Animaciones de entrada
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
  }, { threshold: .12 });
  root.querySelectorAll('[data-gv-reveal]').forEach((el) => io.observe(el));
})();
