

---
layout: default
title: Projects
---

# My GitHub Repositories

{% for repo in site.data.repos %}
## [{{ repo.name }}]({{ repo.html_url }})
- **README**:
  {% if repo.readme %}
  <div class="readme-container">
    <span class="readme-preview" id="preview-{{ repo.name | replace: ' ', '-' | replace: '/', '-' }}">
      {{ repo.readme | slice: 0, 50 }}
      <span class="readme-blur">{{ repo.readme | slice: 50, 20 }}</span>
    </span>
    <span class="readme-full" id="full-{{ repo.name | replace: ' ', '-' | replace: '/', '-' }}" style="display: none;">
      {{ repo.readme }}
    </span>
    <button class="read-more-button" onclick="toggleReadme('{{ repo.name | replace: ' ', '-' | replace: '/', '-' }}')">Read More</button>
  </div>
  {% else %}
  <p>No README available for {{ repo.name }}.</p>
  {% endif %}
{% endfor %}


<script>
function toggleReadme(repoName) {
    const previewId = `preview-${repoName}`;
    const fullId = `full-${repoName}`;

    const preview = document.getElementById(previewId);
    const full = document.getElementById(fullId);
    const button = preview ? preview.nextElementSibling : null;

    // Debugging: Log the elements being accessed
    console.log(`Toggle Readme for: ${repoName}`, { preview, full, button });

    // If elements are not found, log an error and return
    if (!preview || !full || !button) {
        console.error(`Elements not found for repoName: ${repoName}`);
        return;
    }

    // Toggle between preview and full content
    if (preview.style.display === "none") {
        // Show the preview, hide the full content
        preview.style.display = "inline";
        full.style.display = "none";
        button.textContent = "Read More";
    } else {
        // Hide the preview, show the full content
        preview.style.display = "none";
        full.style.display = "inline";
        button.textContent = "Show Less";
    }
}


</script>
