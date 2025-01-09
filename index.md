

---
layout: default
title: Projects
---

# My GitHub Repositories

{% for repo in site.data.repos %}

## [{{ repo.name }}]({{ repo.html_url }})
<div class="code-block-container">
  <div class="code-block-preview styled-code-block" id="preview-{{ repo.name | replace: ' ', '-' | replace: '/', '-' }}">
    {% assign lines = repo.readme | split: '\n' %}
    {% if lines.size > 0 %}
    <div>
      <code>{{ lines[0] }}</code> <!-- First line -->
      {% if lines.size > 1 %}
      <code class="blurred-line">{{ lines[1] }}</code> <!-- Blurred second line -->
      {% endif %}
    </div>
    {% endif %}
  </div>
  <div class="code-block-full styled-code-block" id="full-{{ repo.name | replace: ' ', '-' | replace: '/', '-' }}" style="display: none;">
    <pre>{{ repo.readme | markdownify }}</pre>
  </div>
  <button class="read-more-button" id="button-{{ repo.name | replace: ' ', '-' | replace: '/', '-' }}" onclick="toggleReadme('{{ repo.name | replace: ' ', '-' | replace: '/', '-' }}')">Read More</button>
</div>
{% endfor %}



<script>


function toggleReadme(repoName) {
  const previewId = `preview-${repoName}`;
  const fullId = `full-${repoName}`;
  const butId = `button-${repoName}`;
  
  const preview = document.getElementById(previewId);
  const full = document.getElementById(fullId);
  const button = document.getElementById(butId);

  if (!preview || !full || !button) {
    console.error(`Elements not found for repoName: ${repoName}`);
    return;
  }

  if (preview.style.display === "none") {
    // Show the preview and hide the full content
    preview.style.display = "block";
    full.style.display = "none";
    button.textContent = "Read More";
  } else {
    // Hide the preview and show the full content
    preview.style.display = "none";
    full.style.display = "block";
    button.textContent = "Show Less";
  }
}



</script>
