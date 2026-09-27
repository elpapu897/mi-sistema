
(() => {
  const init = () => document.querySelectorAll('[data-gvn]').forEach(root => {
    if (root.dataset.ready) return;
    root.dataset.ready = 'true';
    const burger = root.querySelector('[data-gvn-burger]');
    const drawer = root.querySelector('[data-gvn-drawer]');
    if (!burger || !drawer) return;
    const close = () => {burger.setAttribute('aria-expanded','false');drawer.hidden=true;};
    burger.addEventListener('click', () => {
      const open = burger.getAttribute('aria-expanded') === 'true';
      burger.setAttribute('aria-expanded', String(!open));drawer.hidden=open;
    });
    drawer.addEventListener('click', event => {if(event.target.closest('a')) close();});
    root.addEventListener('keydown', event => {if(event.key==='Escape'){close();burger.focus();}});
    root.addEventListener('focusout', event => {if(!root.contains(event.relatedTarget)) close();});
    document.addEventListener('pointerdown', event => {if(!root.contains(event.target)) close();});
    window.matchMedia('(min-width:861px)').addEventListener('change', close);
  });
  init();
  document.addEventListener('shopify:section:load', init);
})();
