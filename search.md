---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
title: Search
permalink: /search/
---

<div id="search-searchbar"></div>

<div class="post-list" id="search-hits">
{% for post in site.posts %}
    <div class="post-item">
    {% assign date_format = site.minima.date_format | default: "%b %-d, %Y" %}
    <span class="post-meta">{{ post.date | date: date_format }}</span>

    <h2>
        <a class="post-link" href="{{ post.url | relative_url }}">
        {{ post.title | escape }}
        </a>
    </h2>

    <div class="post-snippet">{{ post.excerpt }}</div>
    </div>
{% endfor %}
</div>

{% include algolia.html %}
