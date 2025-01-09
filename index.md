

---
layout: default
title: Projects
---

# My GitHub Repositories

{% for repo in site.data.repos %}
## [{{ repo.name }}]({{ repo.html_url }})
- **README**:
  <div class="readme-container">
    <div class="readme-preview" id="preview-{{ repo.name }}">
      {{ repo.readme | truncate: 200 }}
    </div>
    <div class="readme-full" id="full-{{ repo.name }}" style="display: none;">
      {{ repo.readme }}
    </div>
    <button class="read-more-button" onclick="toggleReadme('{{ repo.name }}')">Read More</button>
  </div>
{% endfor %}


<script>
function toggleReadme(repoName) {
    const preview = document.getElementById(`preview-${repoName}`);
    const full = document.getElementById(`full-${repoName}`);
    const button = preview.nextElementSibling;

    if (preview.style.display === "none") {
        preview.style.display = "block";
        full.style.display = "none";
        button.textContent = "Read More";
    } else {
        preview.style.display = "none";
        full.style.display = "block";
        button.textContent = "Show Less";
    }
}
</script>
