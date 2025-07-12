// === Theme Toggle ===
const toggleBtn = document.getElementById('themeToggle');
toggleBtn.addEventListener('click', () => {
  document.body.classList.toggle('light-mode');
  toggleBtn.textContent = document.body.classList.contains('light-mode') ? '☀️' : '🌙';
});

// === Redirect Start Button ===
document.getElementById("startBtn").addEventListener("click", () => {
  document.getElementById("nuzeHomepage").classList.add("show");
});
document.getElementById("themeToggle").addEventListener("click", () => {
  document.body.classList.toggle("light-mode");
  document.getElementById("themeToggle").textContent =
    document.body.classList.contains("light-mode") ? "☀️" : "🌙";
});


