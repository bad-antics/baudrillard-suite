---
layout: page
title: Blog
permalink: /blog/
---

# Blog

Security research, tool updates, and technical deep-dives.

---

{% for post in site.posts %}
## [{{ post.title }}]({{ post.url | relative_url }})
<small>{{ post.date | date: "%B %d, %Y" }} • {{ post.categories | join: ", " }}</small>

{{ post.excerpt }}

[Read more →]({{ post.url | relative_url }})

---
{% endfor %}

{% if site.posts.size == 0 %}
*No posts yet. Check back soon!*
{% endif %}
