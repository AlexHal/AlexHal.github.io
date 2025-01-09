

---
layout: default
title: Projects
---

# My GitHub Repositories

{% for repo in site.data.repos %}
## [{{ repo.name }}]({{ repo.html_url }})
<div class="code-block-container">
  <!-- Preview Block -->
  <div class="code-block-preview styled-code-block" id="preview-{{ repo.name | replace: ' ', '-' | replace: '/', '-' }}">
    {% assign normalized_readme = repo.readme | replace: '\n', '
' %}
    {% assign lines = normalized_readme | split: '
' %}

    {% if lines.size > 0 %}
    <pre>
      <div class="blurred-line">{{ lines[0] }}</div> <!-- First line -->
    </pre>
    {% endif %}
  </div>

  <!-- Full Content Block -->
  <div class="code-block-full styled-code-block" id="full-{{ repo.name | replace: ' ', '-' | replace: '/', '-' }}" style="display: none;">
    <pre>{{ repo.readme | markdownify }}</pre>
  </div>

  <!-- Toggle Button -->
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
