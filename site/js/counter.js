const API_URL = "https://2nhm7oe412.execute-api.us-east-1.amazonaws.com/count";

async function updateVisitorCount() {
  const el = document.getElementById("visitor-count");
  if (!el) return;

  const cached = localStorage.getItem("visitor_count");
  const cachedTime = localStorage.getItem("visitor_count_time");
  const ONE_HOUR = 3600000;

  if (cached && cachedTime && (Date.now() - cachedTime < ONE_HOUR)) {
    el.textContent = cached;
    return;
  }

  try {
    const res = await fetch(API_URL);
    const data = await res.json();
    el.textContent = data.count;
    localStorage.setItem("visitor_count", data.count);
    localStorage.setItem("visitor_count_time", Date.now());
  } catch {
    el.textContent = "—";
  }
}

updateVisitorCount();
