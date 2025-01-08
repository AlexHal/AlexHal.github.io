---
layout: default
title: Home
---

# Welcome to My Portfolio
Hello! I'm a developer and this is my portfolio. Here are some of my projects:

# My GitHub Repositories

{% for repo in site.data.repos %}
## [{{ repo.name }}]({{ repo.html_url }})
- **README Preview**:
  <pre>{{ repo.readme | truncate: 500 }}</pre>
{% endfor %