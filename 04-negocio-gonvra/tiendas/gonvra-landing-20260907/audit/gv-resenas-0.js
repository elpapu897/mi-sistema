
(() => {
  document.querySelectorAll('[data-gvr]').forEach((root) => {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { threshold: .1 });
    root.querySelectorAll('[data-gvr-reveal]').forEach((el) => io.observe(el));
  });
})();
