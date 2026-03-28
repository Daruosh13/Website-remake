/**
 * piksort.js
 * Replaces Webflow runtime JS for local hosting.
 * Handles: navigation, hero carousel, solution tabs, Splide carousels,
 *          scroll animations, smooth scroll, video modal.
 */

(function () {
  'use strict';

  /* ───────────────────────────── NAV ───────────────────────────── */

  // Hamburger / mobile menu
  const navBtn  = document.querySelector('.nav_button');
  const navMenu = document.querySelector('.nav_menu');
  const navIcon = navBtn?.querySelector('.menu-icon4_wrapper');

  // Overlay element for clicking outside to close
  const overlay = document.createElement('div');
  overlay.className = 'nav-overlay';
  overlay.style.display = 'none';
  document.body.appendChild(overlay);

  function openMenu() {
    navMenu.classList.add('w--open');
    navBtn.setAttribute('aria-expanded', 'true');
    navIcon?.classList.add('is-open');
    overlay.style.display = 'block';
  }

  function closeMenu() {
    navMenu.classList.remove('w--open');
    navBtn.setAttribute('aria-expanded', 'false');
    navIcon?.classList.remove('is-open');
    overlay.style.display = 'none';
  }

  if (navBtn && navMenu) {
    navBtn.addEventListener('click', () => {
      navMenu.classList.contains('w--open') ? closeMenu() : openMenu();
    });

    // Close when any nav link is clicked
    navMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', closeMenu);
    });
  }

  // Close on overlay click
  overlay.addEventListener('click', closeMenu);

  // Dropdown menus (hover on desktop, click on mobile)
  document.querySelectorAll('.nav_dropdown').forEach(dropdown => {
    const toggle = dropdown.querySelector('.nav_dropdown-toggle');
    const list = dropdown.querySelector('.nav_dropdown-nav');
    if (!toggle || !list) return;

    let closeTimer;

    function openDropdown() {
      clearTimeout(closeTimer);
      list.classList.add('w--open');
      toggle.classList.add('w--open');
    }
    function closeDropdown() {
      closeTimer = setTimeout(() => {
        list.classList.remove('w--open');
        toggle.classList.remove('w--open');
      }, 150);
    }

    if (window.innerWidth >= 992) {
      dropdown.addEventListener('mouseenter', openDropdown);
      dropdown.addEventListener('mouseleave', closeDropdown);
    }
    toggle.addEventListener('click', e => {
      e.stopPropagation();
      const isOpen = list.classList.contains('w--open');
      isOpen ? closeDropdown() : openDropdown();
    });
  });

  // Close dropdowns when clicking outside
  document.addEventListener('click', e => {
    if (!e.target.closest('.nav_dropdown')) {
      document.querySelectorAll('.nav_dropdown-nav.w--open').forEach(el => {
        el.classList.remove('w--open');
        el.previousElementSibling?.classList.remove('w--open');
      });
    }
  });

  /* ─────────────────────── HERO CAROUSEL ──────────────────────── */

  const heroSection = document.querySelector('.section.is-hm-hero');
  const heroCards = heroSection ? [...heroSection.querySelectorAll('.hm-hero_bottom-card')] : [];

  if (heroCards.length) {
    let current = 0;

    function activateHeroCard(index) {
      heroCards.forEach((card, i) => card.classList.toggle('is-active', i === index));
    }

    activateHeroCard(0);

    const heroInterval = setInterval(() => {
      current = (current + 1) % heroCards.length;
      activateHeroCard(current);
    }, 4000);

    // Click to switch
    heroCards.forEach((card, i) => {
      card.addEventListener('click', () => {
        clearInterval(heroInterval);
        current = i;
        activateHeroCard(current);
      });
    });
  }

  /* ──────────────────── SOLUTION TABS ─────────────────────────── */

  document.querySelectorAll('.hm-sol_inner-tab-menu').forEach(tab => {
    tab.addEventListener('click', () => {
      const parentMenu = tab.closest('.hm-sol_tab-menu');
      if (!parentMenu) return;
      const section = parentMenu.closest('.section.is-hm-solutions');
      if (!section) return;

      section.querySelectorAll('.hm-sol_inner-tab-menu').forEach(t => t.classList.remove('is-active'));
      tab.classList.add('is-active');
    });
  });

  // Default: activate first tab
  document.querySelectorAll('.section.is-hm-solutions').forEach(section => {
    const first = section.querySelector('.hm-sol_inner-tab-menu');
    if (first) first.classList.add('is-active');
  });

  /* ────────────────── COMPANY LOGO CAROUSELS ──────────────────── */

  function initSplide(id, direction) {
    const el = document.getElementById(id);
    if (!el) return;
    const splide = new Splide(el, {
      type: 'loop',
      drag: 'free',
      focus: 'center',
      perPage: 5,
      gap: '1rem',
      arrows: false,
      pagination: false,
      autoScroll: {
        speed: direction === 'rtl' ? -0.8 : 0.8,
        pauseOnHover: true,
      },
      breakpoints: {
        767: { perPage: 3 },
        479: { perPage: 2 },
      },
    });
    splide.mount(window.SplideAutoScroll ? { AutoScroll: window.SplideAutoScroll } : {});
  }

  function initTestimonialSplide() {
    const el = document.getElementById('testimonialSplide');
    if (!el) return;
    const splide = new Splide(el, {
      type: 'loop',
      perPage: 1,
      focus: 'center',
      gap: '2rem',
      arrows: false,
      pagination: true,
      autoplay: true,
      interval: 5000,
      pauseOnHover: true,
    });
    splide.mount();
  }

  // Wait for Splide + AutoScroll to load
  function whenSplideReady(cb) {
    if (typeof Splide !== 'undefined') {
      cb();
    } else {
      document.addEventListener('DOMContentLoaded', cb);
    }
  }

  whenSplideReady(() => {
    // AutoScroll extension may be registered as window.SplideAutoScroll
    if (typeof SplideAutoScroll !== 'undefined') {
      Splide.defaults = {};
      // register globally
      window.SplideAutoScroll = SplideAutoScroll;
    }
    initSplide('comp-top', 'rtl');
    initSplide('comp-bottom', 'ltr');
    initTestimonialSplide();
  });

  /* ───────────────── STORY / SCROLL SECTION ───────────────────── */

  const storyItems = document.querySelectorAll('.hm-story_content-item');

  function initStoryScroll() {
    if (!storyItems.length || typeof gsap === 'undefined') return;

    gsap.registerPlugin(ScrollTrigger);

    storyItems.forEach((item, i) => {
      ScrollTrigger.create({
        trigger: item,
        start: 'top center',
        end: 'bottom center',
        onEnter: () => {
          storyItems.forEach(el => el.classList.remove('is-active'));
          item.classList.add('is-active');
        },
        onEnterBack: () => {
          storyItems.forEach(el => el.classList.remove('is-active'));
          item.classList.add('is-active');
        },
      });
    });

    if (storyItems[0]) storyItems[0].classList.add('is-active');
  }

  /* ───────────────── PAIN / SCROLL SECTION ────────────────────── */

  function initPainScroll() {
    if (typeof gsap === 'undefined') return;
    gsap.registerPlugin(ScrollTrigger);

    const painSection = document.querySelector('.section.is-hm-pain');
    if (!painSection) return;

    const contentWrap = painSection.querySelector('.hm-pain_content-wrap');
    if (!contentWrap) return;

    // Pin the section while content scrolls
    ScrollTrigger.create({
      trigger: painSection,
      start: 'top top',
      end: () => '+=' + contentWrap.scrollHeight,
      pin: true,
      scrub: true,
      onUpdate: self => {
        contentWrap.scrollTop = self.progress * (contentWrap.scrollHeight - contentWrap.clientHeight);
      },
    });
  }

  /* ──────────────────── SMOOTH SCROLL LINKS ───────────────────── */

  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', e => {
      const id = link.getAttribute('href').slice(1);
      if (!id) return;
      const target = document.getElementById(id);
      if (!target) return;
      e.preventDefault();
      if (typeof gsap !== 'undefined' && typeof ScrollToPlugin !== 'undefined') {
        gsap.registerPlugin(ScrollToPlugin);
        gsap.to(window, { duration: 1.2, scrollTo: target, ease: 'power2.inOut' });
      } else {
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  /* ─────────────────── STICKY NAV BACKGROUND ──────────────────── */

  const navFixed = document.querySelector('.nav_fixed');
  if (navFixed) {
    const navComponent = navFixed.querySelector('.nav_component');
    window.addEventListener('scroll', () => {
      navComponent?.classList.toggle('is-scrolled', window.scrollY > 40);
    }, { passive: true });
  }

  /* ─────────────────────── VIDEO MODAL ────────────────────────── */

  // Finsweet modal handles this via attributes, but we provide a fallback
  document.querySelectorAll('[fs-modal-element="trigger-1"], [data-modal-trigger]').forEach(trigger => {
    trigger.addEventListener('click', () => {
      const modal = document.getElementById('fs-modal-2-popup');
      if (!modal) return;
      modal.style.display = 'flex';
      // Lazy-load iframe src
      modal.querySelectorAll('iframe[data-src]').forEach(iframe => {
        if (!iframe.src || iframe.src === 'about:blank') {
          iframe.src = iframe.dataset.src.replace('?autoplay=1?', '?autoplay=1&');
        }
      });
    });
  });

  document.querySelectorAll('[fs-modal-element="close-1"]').forEach(close => {
    close.addEventListener('click', () => {
      const modal = close.closest('[fs-modal-element="modal-1"]');
      if (modal) {
        modal.style.display = 'none';
        // Pause video
        modal.querySelectorAll('iframe').forEach(iframe => {
          const src = iframe.src;
          iframe.src = '';
          iframe.src = src;
        });
      }
    });
  });

  /* ──────────────────── SCROLL ANIMATIONS ────────────────────── */

  function initScrollAnimations() {
    if (typeof gsap === 'undefined') return;
    gsap.registerPlugin(ScrollTrigger);

    // Fade-in elements as they enter viewport
    gsap.utils.toArray('.section_header, .hm-clients_card-mini, .hm-feat_item').forEach(el => {
      gsap.fromTo(el,
        { opacity: 0, y: 30 },
        {
          opacity: 1, y: 0, duration: 0.7, ease: 'power2.out',
          scrollTrigger: { trigger: el, start: 'top 85%' }
        }
      );
    });
  }

  /* ─────────────────────── INIT ON READY ─────────────────────── */

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      initStoryScroll();
      initPainScroll();
      initScrollAnimations();
    });
  } else {
    initStoryScroll();
    initPainScroll();
    initScrollAnimations();
  }

})();
