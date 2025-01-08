---
layout: default
title: Projecrs
---

# Welcome to My Portfolio
Hello! I'm a developer and this is my portfolio. Here are some of my projects:

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