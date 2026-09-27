
(() => {
  document.querySelectorAll('[data-gvc]').forEach((root) => {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { threshold: .12 });
    root.querySelectorAll('[data-gvc-reveal]').forEach((el) => io.observe(el));
  });
})();
