{% extends "base.tpl" %}

{% block content %}


<div id="problembar">
{% for problem in problem_list %}
    <div class="problemmargin">
        <div class="problemblock {{ problem.done }}">
            <a class="plink" href="{% url teams.views.problem problem.number %}">{{ problem.number }}</a>
        </div>
    </div>
{% endfor %}
</div>

{{ text }}

{% endblock %}
