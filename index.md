

---
layout: default
title: Projects
---

# My GitHub Repositories

{% for repo in site.data.repos %}
## [{{ repo.name }}]({{ repo.html_url }})
- **README**:
  <div class="readme-container">
    <span class="readme-preview" id="preview-{{ repo.name }}">
      {{ repo.readme | slice: 0, 50 }}
      <span class="readme-blur">{{ repo.readme | slice: 50, 20 }}</span>
    </span>
    <span class="readme-full" id="full-{{ repo.name }}" style="display: none;">
      {{ repo.readme }}
    </span>
    <button class="read-more-button" onclick="toggleReadme('{{ repo.name }}')">Read More</button>
  </div>
{% endfor %}


<script>
function toggleReadme(repoName) {
    const preview = document.getElementById(`preview-${repoName}`);
    const full = document.getElementById(`full-${repoName}`);
    const button = preview.nextElementSibling;

    console.log({ preview, full, button });

    if (!preview || !full || !button) {
        console.error(`Elements not found for repoName: ${repoName}`);
        return;
    }

    if (preview.style.display === "none") {
        preview.style.display = "inline";
        full.style.display = "none";
        button.textContent = "Read More";
    } else {
        preview.style.display = "none";
        full.style.display = "inline";
        button.textContent = "Show Less";
    }
}
</script>
