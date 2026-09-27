
(() => {
  document.querySelectorAll('[data-gva]').forEach((root) => {
    root.querySelectorAll('[data-gva-slider]').forEach((slider) => {
      const input = slider.querySelector('input');
      const before = slider.querySelector('.gva-before .gva-img');
      const sync = () => {
        slider.style.setProperty('--pos', input.value + '%');
        if (before) before.style.setProperty('--w', slider.clientWidth + 'px');
      };
      input.addEventListener('input', sync);
      window.addEventListener('resize', sync);
      sync();
      // barrido de presentación la primera vez que se ve
      const io = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (!e.isIntersecting || slider.dataset.shown) return;
          slider.dataset.shown = '1';
          io.unobserve(slider);
          let v = 50, dir = 1, steps = 0;
          const run = setInterval(() => {
            steps++; v += dir * 2.2;
            if (v >= 74) dir = -1;
            if (v <= 30) dir = 1;
            input.value = v; sync();
            if (steps > 58) { clearInterval(run); input.value = 50; sync(); }
          }, 16);
        });
      }, { threshold: .4 });
      io.observe(slider);
    });
    const reveal = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); reveal.unobserve(e.target); } });
    }, { threshold: .12 });
    root.querySelectorAll('[data-gva-reveal]').forEach((el) => reveal.observe(el));
  });
})();
