{% extends "base.tpl" %}

{% block meta %}
    <link rel="stylesheet" type="text/css" href="/static/sbstyle.css">
    <meta http-equiv="refresh" content="30">
{% endblock %}

{% block content %}

{% for team in teamlist %}
<div class="teamblock">
    <div class="teamname">
        <div class="teamvert">{{ team.name }}</div>
    </div>
    <div class="teamscore">
        <div class="teamvert">{{ team.score }}</div>
    </div>
</div>
{% endfor %}

</table>

{% endblock %}
