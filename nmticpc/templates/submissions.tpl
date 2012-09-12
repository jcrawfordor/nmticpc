{% extends "base.tpl" %}

{% block content %}


<div id="problembar">
{% for problem in problem_list %}
    <div class="problemmargin">
        <div class="problemblock">
            {{ problem.number }}
        </div>
    </div>
{% endfor %}
</div>

{{ text }}

{% endblock %}
