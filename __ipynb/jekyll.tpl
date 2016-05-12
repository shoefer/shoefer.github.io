{% extends 'display_priority.tpl' %}

{%- block header -%}
---
layout: post
title: "{{resources['metadata']['name']}}"
tags:
    - python
    - notebook
use_math: true
---
{%- endblock header -%}

{% block in_prompt %}
**In [{{ cell.prompt_number }}]:**
{% endblock in_prompt %}

{% block output_prompt %}
{%- endblock output_prompt %}

{% block input %}
{{ '{% highlight python %}' }}
{{ cell.input }}
{{ '{% endhighlight %}' }}
{% endblock input %}

{% block pyerr %}
{{ super() }}
{% endblock pyerr %}

{% block traceback_line %}
{{ line | indent | strip_ansi }}
{% endblock traceback_line %}

{% block pyout %}

{% block data_priority scoped %}
{{ super() }}
{% endblock %}
{% endblock pyout %}

{% block stream %}
{{ output.text | indent }}
{% endblock stream %}

{% block data_svg %}
![svg]({{ output.svg_filename | path2support }})
{% endblock data_svg %}

{% block data_png %}
![png]({{ output.png_filename | path2support }})
{% endblock data_png %}

{% block data_jpg %}
![jpeg]({{ output.jpeg_filename | path2support }})
{% endblock data_jpg %}

{% block data_latex %}
{{ output.latex }}
{% endblock data_latex %}

{% block data_html scoped %}
{{ output.html }}
{% endblock data_html %}

{% block data_text scoped %}
{{ output.text | indent }}
{% endblock data_text %}

{% block markdowncell scoped %}
{{ cell.source | wrap_text(80) }}
{% endblock markdowncell %}


{% block headingcell scoped %}
{{ '#' * cell.level }} {{ cell.source | replace('\n', ' ') }}
{% endblock headingcell %}

{% block unknowncell scoped %}
unknown type  {{ cell.type }}
{% endblock unknowncell %}
