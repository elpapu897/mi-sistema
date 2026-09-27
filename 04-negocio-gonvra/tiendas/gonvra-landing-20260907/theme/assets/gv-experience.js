(() => {
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const selector = '[data-gvhm-reveal],[data-gvh-reveal],[data-gvf-reveal],[data-gvd-reveal],[data-gv-reveal],[data-gvb-reveal]';
  const observer = 'IntersectionObserver' in window ? new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.dataset.gvEnter = 'visible';
      observer.unobserve(entry.target);
    });
  }, {threshold: 0, rootMargin: '0px 0px -24px 0px'}) : null;
  const init = (scope = document) => {
    scope.querySelectorAll(selector).forEach(el => {
      if (el.dataset.gvEnter) return;
      if (observer && !motion.matches && el.getBoundingClientRect().top > window.innerHeight && !window.Shopify?.designMode) {
        el.dataset.gvEnter = 'waiting';
        observer.observe(el);
      }
    });
    scope.querySelectorAll('[data-gv-pause]').forEach(button => {
      if (button.dataset.bound) return;
      button.dataset.bound = 'true';
      button.addEventListener('click', () => {
        const paused = button.getAttribute('aria-pressed') !== 'true';
        button.setAttribute('aria-pressed', String(paused));
        button.textContent = paused ? '▶' : 'Ⅱ';
      });
    });
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => init());
  else init();
  document.addEventListener('shopify:section:load', event => init(event.target));
  document.addEventListener('shopify:block:select', event => {
    const target = event.target.closest('[data-gv-enter]');
    if (target) target.dataset.gvEnter = 'visible';
  });
  motion.addEventListener('change', () => {
    if (motion.matches) {
      observer?.disconnect();
      document.querySelectorAll('[data-gv-enter]').forEach(el => { el.dataset.gvEnter = 'visible'; });
    }
  });
})();
