document.addEventListener("DOMContentLoaded", function () {
  if (window.AOS) {
    AOS.init({ duration: 700, once: true, offset: 60 });
  }
  initCounters();

  const geoPanels = document.querySelectorAll("[data-geo-panel]");
  geoPanels.forEach((panel) => {
    panel.addEventListener("click", () => {
      geoPanels.forEach((p) => p.classList.remove("is-active"));
      panel.classList.add("is-active");
    });
  });

  document.querySelectorAll(".wc-extra").forEach((extra) => {
    const row = extra.closest(".wc-row");
    if (row.classList.contains("is-active")) row.classList.add("media-in");
    extra.addEventListener("show.bs.collapse", () => row.classList.add("is-active"));
    extra.addEventListener("shown.bs.collapse", () => row.classList.add("media-in"));
    extra.addEventListener("hide.bs.collapse", () => {
      row.classList.remove("is-active");
      row.classList.remove("media-in");
    });
  });

  const newsList = document.querySelector("[data-news-autoscroll]");
  if (newsList) {
    // Track is rendered twice back-to-back so scrollTop can wrap by exactly
    // one track's height for a seamless upward loop.
    const track = newsList.querySelector(".news-list-track");
    let paused = false;
    let scrollPos = 0;
    newsList.addEventListener("mouseenter", () => { paused = true; });
    newsList.addEventListener("mouseleave", () => { paused = false; });

    function tickNewsScroll() {
      if (!paused) {
        // scrollTop only stores whole pixels, so the sub-pixel step has to be
        // accumulated in JS or it gets rounded away and the list never moves.
        scrollPos += 0.4;
        if (scrollPos >= track.scrollHeight) scrollPos -= track.scrollHeight;
        newsList.scrollTop = scrollPos;
      }
      requestAnimationFrame(tickNewsScroll);
    }
    requestAnimationFrame(tickNewsScroll);
  }
});

// Swiper reads element widths on init, so it must not run until every
// stylesheet (Bootstrap/Swiper CSS pulled from a CDN) has actually applied —
// DOMContentLoaded fires too early for that and leaves carousels measuring a
// pre-layout width that never gets corrected. `load` waits for everything.
window.addEventListener("load", function () {
  if (!window.Swiper) return;

  if (document.querySelector(".ticker-swiper")) {
    // Same align-items:center + autoplay resize-observer trap as the
    // testimonial carousel (see below) — disable the observer defensively.
    new Swiper(".ticker-swiper", {
      loop: true,
      autoplay: { delay: 4500, disableOnInteraction: false },
      speed: 600,
      allowTouchMove: false,
      resizeObserver: false,
      observer: false,
      navigation: { prevEl: ".ticker-prev", nextEl: ".ticker-next" },
    });
  }

  if (document.querySelector(".stats-banner-swiper")) {
    new Swiper(".stats-banner-swiper", {
      loop: true,
      slidesPerView: "auto",
      spaceBetween: 40,
      speed: 4000,
      autoplay: { delay: 0, disableOnInteraction: false },
      allowTouchMove: false,
      resizeObserver: false,
      observer: false,
      breakpoints: {
        768: { spaceBetween: 100 },
        1200: { spaceBetween: 180 },
      },
    });
  }

  if (document.querySelector(".legacy-media-swiper")) {
    new Swiper(".legacy-media-swiper", {
      loop: true,
      slidesPerGroup: 1,
      spaceBetween: 20,
      speed: 600,
      autoplay: { delay: 4500, disableOnInteraction: false },
      resizeObserver: false,
      observer: false,
      navigation: { prevEl: ".legacy-media-prev", nextEl: ".legacy-media-next" },
      slidesPerView: 1,
      breakpoints: {
        640: { slidesPerView: 2 },
        992: { slidesPerView: 3 },
      },
    });
  }

  if (document.querySelector(".research-media-swiper")) {
    new Swiper(".research-media-swiper", {
      loop: true,
      slidesPerGroup: 1,
      spaceBetween: 20,
      speed: 600,
      autoplay: { delay: 4500, disableOnInteraction: false },
      resizeObserver: false,
      observer: false,
      navigation: { prevEl: ".research-media-prev", nextEl: ".research-media-next" },
      slidesPerView: 1,
      breakpoints: {
        640: { slidesPerView: 2 },
        992: { slidesPerView: 3 },
      },
    });
  }

  if (document.querySelector(".spotlight-swiper")) {
    new Swiper(".spotlight-swiper", {
      loop: true,
      slidesPerGroup: 1,
      spaceBetween: 24,
      speed: 600,
      autoplay: { delay: 5000, disableOnInteraction: false },
      resizeObserver: false,
      observer: false,
      navigation: { prevEl: ".spotlight-prev", nextEl: ".spotlight-next" },
      slidesPerView: 1,
      breakpoints: {
        768: { slidesPerView: 2 },
      },
    });
  }

  if (document.querySelector(".aerial-swiper")) {
    new Swiper(".aerial-swiper", {
      loop: true,
      speed: 800,
      autoplay: { delay: 4200, disableOnInteraction: false },
      pagination: { el: ".aerial-pagination", clickable: true },
      resizeObserver: false,
      observer: false,
    });
  }

  if (document.querySelector(".pso-swiper")) {
    new Swiper(".pso-swiper", {
      loop: true,
      slidesPerView: 2,
      spaceBetween: 14,
      speed: 600,
      autoplay: { delay: 4500, disableOnInteraction: false },
      resizeObserver: false,
      observer: false,
      navigation: { prevEl: ".pso-prev", nextEl: ".pso-next" },
      breakpoints: {
        576: { spaceBetween: 20 },
        992: { spaceBetween: 24 },
      },
    });
  }

  if (document.querySelector(".news-feature-swiper")) {
    const newsMeta = document.querySelector("[data-news-meta]");
    const newsHeadline = document.querySelector("[data-news-headline]");
    const newsCta = document.querySelector("[data-news-cta]");

    new Swiper(".news-feature-swiper", {
      loop: true,
      speed: 600,
      autoplay: { delay: 5000, disableOnInteraction: false },
      resizeObserver: false,
      observer: false,
      navigation: { prevEl: ".news-feature-prev", nextEl: ".news-feature-next" },
      on: {
        slideChange(sw) {
          const active = sw.slides[sw.activeIndex];
          if (!active || !active.dataset.headline) return;
          newsMeta.textContent = active.dataset.date;
          newsHeadline.textContent = active.dataset.headline;
          newsHeadline.setAttribute("href", active.dataset.headlineUrl);
          newsCta.childNodes[0].textContent = active.dataset.ctaLabel + " ";
          newsCta.setAttribute("href", active.dataset.ctaUrl);
        },
      },
    });
  }

  if (document.querySelector(".drive-swiper")) {
    new Swiper(".drive-swiper", {
      loop: true,
      slidesPerGroup: 1,
      spaceBetween: 32,
      speed: 600,
      autoplay: { delay: 5000, disableOnInteraction: false },
      resizeObserver: false,
      observer: false,
      navigation: { prevEl: ".drive-prev", nextEl: ".drive-next" },
      slidesPerView: 1,
      breakpoints: {
        640: { slidesPerView: 2 },
        992: { slidesPerView: 3 },
      },
    });
  }

  if (document.querySelector(".pride-slider-swiper")) {
    // Same flex align-items:center + autoplay resize-observer trap as the
    // ticker/testimonial carousels — disable the observer defensively.
    new Swiper(".pride-slider-swiper", {
      loop: true,
      autoplay: { delay: 4000, disableOnInteraction: false },
      speed: 600,
      pagination: { el: ".pride-slider-pagination", clickable: true },
      resizeObserver: false,
      observer: false,
    });
  }

  if (document.querySelector(".hero-swiper")) {
    new Swiper(".hero-swiper", {
      loop: true,
      autoplay: { delay: 6000, disableOnInteraction: false },
      speed: 800,
      pagination: { el: ".hero-pagination", clickable: true },
    });
  }

  if (document.querySelector(".companies-swiper")) {
    new Swiper(".companies-swiper", {
      loop: true,
      slidesPerView: "auto",
      spaceBetween: 20,
      speed: 4000,
      autoplay: { delay: 0, disableOnInteraction: false },
      allowTouchMove: false,
      resizeObserver: false,
      observer: false,
    });
  }

  if (document.querySelector(".dept-course-swiper")) {
    // Department course/faculty counts come from data, so loop only once there
    // are more slides than the widest breakpoint shows — otherwise Swiper
    // disables loop and logs a warning on a department with two courses.
    const courseCount = document.querySelectorAll(".dept-course-swiper .swiper-slide").length;
    new Swiper(".dept-course-swiper", {
      loop: courseCount > 3,
      speed: 600,
      spaceBetween: 24,
      autoplay: { delay: 4500, disableOnInteraction: false },
      // A department with fewer courses than the breakpoint shows would leave
      // them jammed left against a gap; centre them in the track instead.
      centerInsufficientSlides: true,
      resizeObserver: false,
      observer: false,
      navigation: { prevEl: ".dept-course-prev", nextEl: ".dept-course-next" },
      pagination: { el: ".dept-course-pagination", clickable: true },
      slidesPerView: 1,
      breakpoints: {
        576: { slidesPerView: 2 },
        992: { slidesPerView: 3 },
      },
    });
  }

  if (document.querySelector(".dept-faculty-swiper")) {
    const facultyCount = document.querySelectorAll(".dept-faculty-swiper .swiper-slide").length;
    new Swiper(".dept-faculty-swiper", {
      loop: facultyCount > 4,
      speed: 600,
      spaceBetween: 22,
      autoplay: { delay: 4000, disableOnInteraction: false },
      centerInsufficientSlides: true,
      resizeObserver: false,
      observer: false,
      navigation: { prevEl: ".dept-faculty-prev", nextEl: ".dept-faculty-next" },
      pagination: { el: ".dept-faculty-pagination", clickable: true },
      slidesPerView: 1,
      breakpoints: {
        576: { slidesPerView: 2 },
        992: { slidesPerView: 3 },
        1200: { slidesPerView: 4 },
      },
    });
  }

  if (document.querySelector(".mentors-swiper")) {
    // The name/role/stat live outside the carousel (bottom-left of the hero),
    // so they are driven off the active slide's dataset — same approach as the
    // news feature carousel above.
    const setMentorText = (selector, value) => {
      const el = document.querySelector(selector);
      if (el) el.textContent = value || "";
    };

    new Swiper(".mentors-swiper", {
      loop: true,
      speed: 700,
      autoplay: { delay: 4000, disableOnInteraction: false },
      resizeObserver: false,
      observer: false,
      navigation: { prevEl: ".mentors-prev", nextEl: ".mentors-next" },
      pagination: { el: ".mentors-pagination", clickable: true },
      on: {
        slideChange(sw) {
          const active = sw.slides[sw.activeIndex];
          if (!active) return;
          setMentorText("[data-mentor-name]", active.dataset.name);
          setMentorText("[data-mentor-role]", active.dataset.role);
          setMentorText("[data-mentor-stat-label]", active.dataset.statLabel);
          setMentorText("[data-mentor-stat-value]", active.dataset.statValue);
          const stat = document.querySelector("[data-mentor-stat]");
          if (stat) stat.hidden = !active.dataset.statValue;
        },
      },
    });
  }

  if (document.querySelector(".alumni-swiper")) {
    const alumniThumbs = document.querySelectorAll(".alumni-thumb");
    const alumniSwiper = new Swiper(".alumni-swiper", {
      loop: true,
      speed: 600,
      resizeObserver: false,
      observer: false,
      navigation: { prevEl: ".alumni-prev", nextEl: ".alumni-next" },
      on: {
        slideChange(sw) {
          alumniThumbs.forEach((thumb, i) => thumb.classList.toggle("is-active", i === sw.realIndex));
        },
      },
    });
    alumniThumbs.forEach((thumb, i) => {
      thumb.addEventListener("click", () => alumniSwiper.slideToLoop(i));
    });
  }
});

function animateCounter(el) {
  const match = el.textContent.trim().match(/^([\d,]+)(.*)$/);
  if (!match) return;
  const target = parseInt(match[1].replace(/,/g, ""), 10);
  const suffix = match[2];
  const duration = 1400;
  const startTime = performance.now();

  function step(now) {
    const progress = Math.min((now - startTime) / duration, 1);
    const value = Math.floor(progress * target);
    el.textContent = value.toLocaleString() + suffix;
    if (progress < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

function initCounters() {
  const counters = document.querySelectorAll("[data-count]");
  if (!counters.length || !window.IntersectionObserver) return;
  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          obs.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.4 }
  );
  counters.forEach((el) => observer.observe(el));
}
