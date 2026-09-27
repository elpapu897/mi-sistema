
(() => {
  document.querySelectorAll('[data-gvd]').forEach((root) => {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        e.target.classList.add('is-in');
        const num = e.target.querySelector('[data-gvd-num]');
        if (num && !num.dataset.done) {
          const raw = num.dataset.gvdNum;
          const target = parseInt(String(raw).replace(/\D/g, ''), 10);
          if (!isNaN(target) && target > 0 && target < 100000) {
            num.dataset.done = '1';
            const suffix = num.textContent.replace(String(raw), '');
            let step = 0;
            const total = 34;
            const run = setInterval(() => {
              step++;
              const value = Math.round((target * step) / total);
              num.textContent = value + suffix;
              if (step >= total) { clearInterval(run); num.textContent = raw + suffix; }
            }, 22);
          }
        }
        io.unobserve(e.target);
      });
    }, { threshold: .25 });
    root.querySelectorAll('[data-gvd-reveal]').forEach((el) => io.observe(el));
  });
})();
