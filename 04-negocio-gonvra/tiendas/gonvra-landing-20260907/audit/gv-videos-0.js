
(() => {
  document.querySelectorAll('[data-gvv]').forEach((root) => {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { threshold: .12 });
    root.querySelectorAll('[data-gvv-reveal]').forEach((el) => io.observe(el));

    const box = root.querySelector('[data-gvv-lightbox]');
    const stage = root.querySelector('[data-gvv-stage]');
    const cerrar = () => { box.hidden = true; stage.innerHTML = ''; document.body.style.overflow = ''; };
    root.querySelectorAll('[data-gvv-zoom]').forEach((btn) => {
      btn.addEventListener('click', () => {
        const media = btn.parentElement.querySelector('img, video');
        if (!media || !box) return;
        stage.innerHTML = '';
        stage.appendChild(media.cloneNode(true));
        box.hidden = false;
        document.body.style.overflow = 'hidden';
      });
    });
    root.querySelector('[data-gvv-close]')?.addEventListener('click', cerrar);
    box?.addEventListener('click', (e) => { if (e.target === box) cerrar(); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && box && !box.hidden) cerrar(); });
  });
})();
