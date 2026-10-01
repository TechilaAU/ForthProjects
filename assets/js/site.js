(function () {
  "use strict";

  // Mobile nav
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("open", !open);
      document.body.style.overflow = open ? "" : "hidden";
    });
  }

  // Dropdowns
  var btns = document.querySelectorAll(".dd-btn");
  function closeAll(except) {
    btns.forEach(function (b) { if (b !== except) b.setAttribute("aria-expanded", "false"); });
  }
  btns.forEach(function (b) {
    b.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = b.getAttribute("aria-expanded") === "true";
      closeAll(b);
      b.setAttribute("aria-expanded", String(!open));
    });
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".has-dd")) closeAll();
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      var openBtn = document.querySelector('.dd-btn[aria-expanded="true"]');
      closeAll();
      if (openBtn) openBtn.focus();
    }
  });

  // Year
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Forms: POST to endpoint as JSON; fall back to a prefilled email if no endpoint is configured.
  document.querySelectorAll("form[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".form-status");
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var fd = new FormData(form);
      if (fd.get("_gotcha")) return;
      var data = {};
      fd.forEach(function (v, k) {
        if (k === "_gotcha") return;
        data[k] = data[k] ? data[k] + ", " + v : v;
      });
      var endpoint = form.getAttribute("action") || "";
      var btn = form.querySelector('button[type="submit"]');
      if (!/^https?:\/\//.test(endpoint)) {
        var body = Object.keys(data).filter(function (k) { return k !== "_subject"; })
          .map(function (k) { return k + ": " + data[k]; }).join("\n");
        window.location.href = "mailto:" + form.getAttribute("data-mailto") +
          "?subject=" + encodeURIComponent(data._subject || "Website enquiry") + "&body=" + encodeURIComponent(body);
        return;
      }
      btn.disabled = true;
      status.className = "form-status";
      status.textContent = "Sending your details...";
      fetch(endpoint, { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(data) })
        .then(function (r) {
          if (!r.ok) throw new Error();
          form.reset();
          status.className = "form-status ok";
          status.textContent = "Thanks. Your details have been sent and we'll be in touch within one business day.";
          if (window.dataLayer) window.dataLayer.push({ event: "form_submit", form: data._subject });
        })
        .catch(function () {
          status.className = "form-status err";
          status.textContent = "Your details weren't sent. Check your connection and try again, or email " + form.getAttribute("data-mailto") + ".";
        })
        .finally(function () { btn.disabled = false; });
    });
  });

  // Project filters
  var list = document.querySelector("[data-projects]");
  if (list) {
    var selects = document.querySelectorAll("[data-filter]");
    var empty = document.querySelector("[data-empty]");
    var apply = function () {
      var f = {};
      selects.forEach(function (s) { f[s.getAttribute("data-filter")] = s.value; });
      var shown = 0;
      list.querySelectorAll("li").forEach(function (li) {
        var ok = (!f.service || li.dataset.service === f.service) && (!f.sector || li.dataset.sector === f.sector);
        li.hidden = !ok; if (ok) shown++;
      });
      if (empty) empty.hidden = shown !== 0;
    };
    selects.forEach(function (s) { s.addEventListener("change", apply); });
  }
})();
