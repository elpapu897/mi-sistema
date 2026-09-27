(() => {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const moneyFallback = (cents) => {
    const amount = Number(cents || 0) / 100;
    return new Intl.NumberFormat(document.documentElement.lang || 'es', {
      style: 'currency',
      currency: window.Shopify?.currency?.active || 'ARS'
    }).format(amount);
  };

  function initReveals(root = document) {
    const items = [...root.querySelectorAll('.mt-reveal:not([data-mt-ready])')];
    if (!items.length) return;
    items.forEach((item) => item.dataset.mtReady = 'true');

    if (prefersReducedMotion || !('IntersectionObserver' in window)) {
      items.forEach((item) => item.classList.add('mt-visible'));
      return;
    }

    const observer = new IntersectionObserver((entries, currentObserver) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('mt-visible');
        currentObserver.unobserve(entry.target);
      });
    }, { threshold: 0.16, rootMargin: '0px 0px -5% 0px' });

    items.forEach((item) => observer.observe(item));
  }

  function initCounters(root = document) {
    const counters = [...root.querySelectorAll('[data-mt-count]:not([data-mt-count-ready])')];
    if (!counters.length) return;
    counters.forEach((counter) => counter.dataset.mtCountReady = 'true');

    const run = (counter) => {
      const target = Number(counter.dataset.mtCount || 0);
      const suffix = counter.dataset.mtSuffix || '';
      const decimals = Number(counter.dataset.mtDecimals || 0);
      if (prefersReducedMotion) {
        counter.textContent = `${target.toFixed(decimals)}${suffix}`;
        return;
      }
      const start = performance.now();
      const duration = 1200;
      const tick = (now) => {
        const progress = Math.min(1, (now - start) / duration);
        const eased = 1 - Math.pow(1 - progress, 3);
        counter.textContent = `${(target * eased).toFixed(decimals)}${suffix}`;
        if (progress < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };

    if (!('IntersectionObserver' in window)) {
      counters.forEach(run);
      return;
    }
    const observer = new IntersectionObserver((entries, currentObserver) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        run(entry.target);
        currentObserver.unobserve(entry.target);
      });
    }, { threshold: 0.5 });
    counters.forEach((counter) => observer.observe(counter));
  }

  function initTilt(root = document) {
    if (prefersReducedMotion || !window.matchMedia('(pointer: fine)').matches) return;
    root.querySelectorAll('[data-mt-tilt]:not([data-mt-tilt-ready])').forEach((card) => {
      card.dataset.mtTiltReady = 'true';
      const strength = Number(card.dataset.mtTilt || 5);
      card.addEventListener('pointermove', (event) => {
        const rect = card.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width - 0.5;
        const y = (event.clientY - rect.top) / rect.height - 0.5;
        card.style.transform = `perspective(900px) rotateX(${(-y * strength).toFixed(2)}deg) rotateY(${(x * strength).toFixed(2)}deg) translateY(-4px)`;
      });
      card.addEventListener('pointerleave', () => {
        card.style.transform = '';
      });
    });
  }

  function initParallax(root = document) {
    const items = [...root.querySelectorAll('[data-mt-parallax]:not([data-mt-parallax-ready])')];
    if (!items.length || prefersReducedMotion || !window.matchMedia('(pointer: fine)').matches) return;
    items.forEach((item) => item.dataset.mtParallaxReady = 'true');
    let ticking = false;
    const update = () => {
      items.forEach((item) => {
        const rect = item.getBoundingClientRect();
        if (rect.bottom < 0 || rect.top > window.innerHeight) return;
        const intensity = Number(item.dataset.mtParallax || 12);
        const center = rect.top + rect.height / 2;
        const offset = (center - window.innerHeight / 2) / window.innerHeight;
        item.style.transform = `translate3d(0, ${(offset * intensity).toFixed(1)}px, 0) scale(1.035)`;
      });
      ticking = false;
    };
    window.addEventListener('scroll', () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(update);
    }, { passive: true });
    update();
  }

  function initProductGallery(root = document) {
    root.querySelectorAll('[data-mt-gallery]:not([data-mt-gallery-ready])').forEach((gallery) => {
      gallery.dataset.mtGalleryReady = 'true';
      const main = gallery.querySelector('[data-mt-gallery-main]');
      if (!main) return;
      gallery.querySelectorAll('[data-mt-gallery-thumb]').forEach((thumb) => {
        thumb.addEventListener('click', () => {
          const nextSrc = thumb.dataset.src;
          const nextSrcset = thumb.dataset.srcset || '';
          const nextAlt = thumb.dataset.alt || '';
          if (!nextSrc) return;
          main.style.opacity = '0';
          window.setTimeout(() => {
            main.src = nextSrc;
            if (nextSrcset) main.srcset = nextSrcset;
            else main.removeAttribute('srcset');
            main.alt = nextAlt;
            main.style.opacity = '1';
          }, 150);
          gallery.querySelectorAll('[data-mt-gallery-thumb]').forEach((button) => button.classList.remove('is-active'));
          thumb.classList.add('is-active');
        });
      });
    });
  }

  function initProductVariants(root = document) {
    root.querySelectorAll('[data-mt-product]:not([data-mt-product-ready])').forEach((section) => {
      section.dataset.mtProductReady = 'true';
      const dataNode = section.querySelector('[data-mt-variants-json]');
      const form = section.querySelector('form[action*="/cart/add"]');
      if (!dataNode || !form) return;

      let variants = [];
      try { variants = JSON.parse(dataNode.textContent); } catch (error) { return; }
      const optionGroups = [...section.querySelectorAll('[data-mt-option-group]')];
      const optionInputs = [...section.querySelectorAll('[data-mt-option]')];
      const variantInput = form.querySelector('[name="id"]');
      const quantityInput = form.querySelector('[data-mt-quantity]');
      const price = section.querySelector('[data-mt-price]');
      const comparePrice = section.querySelector('[data-mt-compare-price]');
      const stockState = section.querySelector('[data-mt-stock-state]');
      const stockDetail = (stockState?.textContent.split('·')[0] || '').trim();
      const submit = form.querySelector('[type="submit"]');
      const submitText = submit?.querySelector('[data-mt-submit-text]');
      const galleryThumbs = [...section.querySelectorAll('[data-mt-gallery-thumb]')];
      const offerButtons = [...form.querySelectorAll('[data-mt-offer]')];
      const offerPrices = [...form.querySelectorAll('[data-mt-offer-price]')];
      const offerUnitPrices = [...form.querySelectorAll('[data-mt-offer-unit-price]')];
      const colorIndex = optionGroups.findIndex((group) => ['color', 'colour'].includes(group.dataset.mtOptionName));
      let selectedQuantity = Math.max(1, Number(quantityInput?.value || 1));
      let activeVariant = variants[0];

      const selectedOptions = () => optionGroups.map((group) => {
        const selected = group.querySelector('[data-mt-option]:checked');
        return (selected || group.querySelector('[data-mt-option]'))?.value || '';
      });

      const purchaseText = (available) => {
        if (!available) return section.dataset.soldOutText || 'Agotado';
        if (selectedQuantity === 1) return section.dataset.addText || 'Agregar al carrito';
        return (section.dataset.addMultipleText || 'Agregar [cantidad] unidades al carrito').replace('[cantidad]', selectedQuantity);
      };

      const syncOfferPrices = (variant) => {
        if (!variant) return;
        offerPrices.forEach((priceNode) => {
          const quantity = Math.max(1, Number(priceNode.dataset.mtOfferPrice || 1));
          priceNode.textContent = moneyFallback(Number(variant.price || 0) * quantity);
        });
        offerUnitPrices.forEach((priceNode) => {
          priceNode.textContent = `${variant.priceFormatted || moneyFallback(variant.price)} c/u`;
        });
      };

      const syncOfferState = () => {
        if (quantityInput) quantityInput.value = selectedQuantity;
        offerButtons.forEach((button) => {
          const isActive = Number(button.dataset.mtQuantityValue || 1) === selectedQuantity;
          button.classList.toggle('is-active', isActive);
          button.setAttribute('aria-pressed', String(isActive));
        });
        if (submitText) submitText.textContent = purchaseText(activeVariant?.available);
      };

      const syncGallery = (variant) => {
        let target = null;
        if (colorIndex >= 0 && variant.options[colorIndex]) {
          const selectedColor = variant.options[colorIndex].toLowerCase();
          const colorTerms = selectedColor.includes('green') || selectedColor.includes('verde')
            ? ['green', 'verde']
            : selectedColor.includes('silver') || selectedColor.includes('platead')
              ? ['silver', 'platead']
              : [selectedColor];
          target = galleryThumbs.find((thumb) => {
            const alt = (thumb.dataset.alt || '').toLowerCase();
            return colorTerms.some((term) => alt.includes(term));
          });
        }
        if (!target && variant.featuredMediaId) {
          target = galleryThumbs.find((thumb) => thumb.dataset.mediaId === String(variant.featuredMediaId));
        }
        if (target && !target.classList.contains('is-active')) target.click();
      };

      const update = () => {
        const selected = selectedOptions();
        const variant = optionGroups.length
          ? variants.find((item) => item.options.every((value, index) => value === selected[index]))
          : variants[0];
        if (!variant) {
          if (submit) submit.disabled = true;
          if (submitText) submitText.textContent = section.dataset.unavailableText || 'No disponible';
          if (stockState) stockState.textContent = section.dataset.unavailableText || 'No disponible';
          return;
        }
        activeVariant = variant;
        if (variantInput) {
          variantInput.value = variant.id;
          variantInput.disabled = !variant.available;
        }
        if (price) price.textContent = variant.priceFormatted || moneyFallback(variant.price);
        if (comparePrice) {
          comparePrice.textContent = variant.compareAtPriceFormatted || '';
          comparePrice.hidden = !variant.compareAtPriceFormatted;
        }
        if (submit) submit.disabled = !variant.available;
        if (submitText) submitText.textContent = purchaseText(variant.available);
        if (stockState) {
          const availability = variant.available
            ? (section.dataset.inStockText || 'En stock')
            : (section.dataset.outOfStockText || 'Agotado');
          stockState.textContent = stockDetail ? `${stockDetail} · ${availability}` : availability;
        }
        syncGallery(variant);
        syncOfferPrices(variant);
        const url = new URL(window.location.href);
        url.searchParams.set('variant', variant.id);
        window.history.replaceState({}, '', url.toString());
      };

      optionInputs.forEach((input) => input.addEventListener('change', update));
      offerButtons.forEach((button) => button.addEventListener('click', () => {
        selectedQuantity = Math.max(1, Number(button.dataset.mtQuantityValue || 1));
        syncOfferState();
      }));
      update();
      syncOfferState();
    });
  }

  function init(root = document) {
    initReveals(root);
    initCounters(root);
    initTilt(root);
    initParallax(root);
    initProductGallery(root);
    initProductVariants(root);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => init());
  else init();

  document.addEventListener('shopify:section:load', (event) => init(event.target));
})();
