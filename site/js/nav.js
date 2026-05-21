document.querySelector('.nav-toggle').addEventListener('click', function() {
  document.querySelector('.nav-links').classList.toggle('open');
});

// Preserve query params (e.g. ?token=...) across page navigation
(function() {
  var qs = window.location.search;
  if (!qs) return;
  document.querySelectorAll('a[href]').forEach(function(a) {
    var href = a.getAttribute('href');
    if (href && href.endsWith('.html') && !href.startsWith('http')) {
      a.setAttribute('href', href + qs);
    }
  });
})();
