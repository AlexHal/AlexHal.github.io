

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
  
  console.log(`Trying to access preview: ${previewId}, full: ${fullId}`);
  
  const preview = document.getElementById(previewId);
  const full = document.getElementById(fullId);
  const button = preview ? preview.nextElementSibling : null;

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
