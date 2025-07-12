// === Theme Toggle ===
const toggleBtn = document.getElementById('themeToggle');
toggleBtn.addEventListener('click', () => {
  document.body.classList.toggle('light-mode');
  toggleBtn.textContent = document.body.classList.contains('light-mode') ? '☀️' : '🌙';
});

// === Start App Button Logic ===
document.getElementById("startBtn").addEventListener("click", () => {
  // Hide hero section
  document.getElementById("landing").style.display = "none";

  // Show main app section
  const app = document.getElementById("mainApp");
  app.classList.remove("hidden");
  app.style.display = "block";

  // Optional: scroll to top smoothly
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// === Handle Pasted Article ===
function handlePaste() {
  const pastedText = prompt("Paste your article content:");
  if (pastedText) {
    fetch('/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ article: pastedText })
    })
    .then(res => res.json())
    .then(data => {
      document.getElementById('searchResults').innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    })
    .catch(error => {
      document.getElementById('searchResults').innerHTML = `<p style="color:red;">Failed to analyze: ${error.message}</p>`;
    });
  }
}

// === Handle File Upload ===
document.getElementById('fileInput').addEventListener('change', function () {
  const file = this.files[0];
  if (file) {
    const formData = new FormData();
    formData.append("file", file);
    fetch('/upload', {
      method: 'POST',
      body: formData
    })
    .then(res => res.json())
    .then(data => {
      document.getElementById('searchResults').innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    })
    .catch(error => {
      document.getElementById('searchResults').innerHTML = `<p style="color:red;">Upload failed: ${error.message}</p>`;
    });
  }
});

function submitAnalyzeForm() {
  const form = document.getElementById('your-form-id');
  fetch('/analyze', {
    method: 'POST',
    body: new FormData(form)
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      // Show the extracted text on the page
      document.getElementById('searchResults').innerHTML = `<pre>${data.text}</pre>`;
    } else {
      document.getElementById('searchResults').innerHTML = `<p style="color:red;">${data.error}</p>`;
      console.error(data.error);
    }
  })
  .catch(error => {
    document.getElementById('searchResults').innerHTML = `<p style="color:red;">Something went wrong: ${error.message}</p>`;
    console.error("Something went wrong:", error);
  });
}

document.getElementById('newsLinkForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const form = e.target;
  fetch('/analyze', {
    method: 'POST',
    body: new FormData(form)
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      document.getElementById('searchResults').innerHTML = `<pre>${data.text}</pre>`;
    } else {
      document.getElementById('searchResults').innerHTML = `<p style="color:red;">${data.error}</p>`;
    }
  })
  .catch(error => {
    document.getElementById('searchResults').innerHTML = `<p style="color:red;">Failed to analyze: ${error.message}</p>`;
  });
});


