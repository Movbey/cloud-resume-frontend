const API_URL = "https://2nhm7oe412.execute-api.us-east-1.amazonaws.com/count";

async function updateVisitorCount() {
  try {
    const res = await fetch(API_URL);
    const data = await res.json();
    document.getElementById("visitor-count").textContent = data.count;
  } catch {
    document.getElementById("visitor-count").textContent = "—";
  }
}

updateVisitorCount();
