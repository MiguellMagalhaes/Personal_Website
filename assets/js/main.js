/**
 * Personal portfolio scripts
 * Based on MyResume template by BootstrapMade.com
 */

(function() {
  "use strict";

  const headerToggleBtn = document.querySelector('.header-toggle');

  function headerToggle() {
    const header = document.querySelector('#header');
    const isOpen = header.classList.toggle('header-show');
    headerToggleBtn.classList.toggle('bi-list');
    headerToggleBtn.classList.toggle('bi-x');
    headerToggleBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  }

  if (headerToggleBtn) {
    headerToggleBtn.addEventListener('click', headerToggle);
    headerToggleBtn.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        headerToggle();
      }
    });
  }

  document.querySelectorAll('#navmenu a').forEach((navmenu) => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.header-show')) {
        headerToggle();
      }
    });
  });

  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  const scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }

  if (scrollTop) {
    scrollTop.addEventListener('click', (event) => {
      event.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  const selectTyped = document.querySelector('.typed');
  if (selectTyped) {
    const typedStrings = selectTyped.getAttribute('data-typed-items').split(',');
    new Typed('.typed', {
      strings: typedStrings,
      loop: true,
      typeSpeed: 100,
      backSpeed: 50,
      backDelay: 2000
    });
  }

  if (typeof PureCounter !== 'undefined') {
    new PureCounter();
  }

  function initSwiper() {
    document.querySelectorAll('.init-swiper').forEach(function(swiperElement) {
      const configElement = swiperElement.querySelector('.swiper-config');
      if (!configElement) {
        return;
      }

      const config = JSON.parse(configElement.innerHTML.trim());
      new Swiper(swiperElement, config);
    });
  }

  window.addEventListener('load', initSwiper);

  window.addEventListener('load', function() {
    if (window.location.hash) {
      const section = document.querySelector(window.location.hash);
      if (section) {
        setTimeout(() => {
          const scrollMarginTop = getComputedStyle(section).scrollMarginTop;
          window.scrollTo({
            top: section.offsetTop - parseInt(scrollMarginTop, 10),
            behavior: 'smooth'
          });
        }, 100);
      }
    }
  });

  const navmenulinks = document.querySelectorAll('.navmenu a');

  function navmenuScrollspy() {
    navmenulinks.forEach((navmenulink) => {
      if (!navmenulink.hash) {
        return;
      }

      const section = document.querySelector(navmenulink.hash);
      if (!section) {
        return;
      }

      const position = window.scrollY + 200;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach((link) => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    });
  }

  window.addEventListener('load', navmenuScrollspy);
  document.addEventListener('scroll', navmenuScrollspy);

  const portfolioFilterButtons = document.querySelectorAll('.portfolio-filter-btn');
  const portfolioItems = document.querySelectorAll('.my-portfolio-item[data-categories]');

  portfolioFilterButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const filter = button.getAttribute('data-filter');

      portfolioFilterButtons.forEach((btn) => {
        btn.classList.remove('active');
        btn.setAttribute('aria-selected', 'false');
      });
      button.classList.add('active');
      button.setAttribute('aria-selected', 'true');

      portfolioItems.forEach((item) => {
        const categories = item.getAttribute('data-categories') || '';
        const match = filter === 'all' || categories.split(' ').includes(filter);
        item.classList.toggle('is-hidden', !match);
      });
    });
  });

  const copyEmailBtn = document.querySelector('.btn-copy-email');
  const copyEmailFeedback = document.querySelector('.copy-email-feedback');
  const emailAddress = 'miguel.softeng@gmail.com';

  if (copyEmailBtn) {
    copyEmailBtn.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(emailAddress);
        if (copyEmailFeedback) {
          copyEmailFeedback.textContent = 'Email copied to clipboard.';
        }
      } catch (error) {
        if (copyEmailFeedback) {
          copyEmailFeedback.textContent = 'Could not copy email. Please copy manually.';
        }
      }
    });
  }
})();
