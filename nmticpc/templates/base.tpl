<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
    <title>{{ title }} -- NMT ICPC Practice</title>
    <link rel="stylesheet" type="text/css" href="/static/mainstyle.css">
    {% block meta %}{% endblock %}
</head>
<body>
    <div id="container">
        <div id="header">
            NMT ICPC
            <div id="userinfo">{% if user.is_authenticated %} {{ user.username }} (<a href="/accounts/signout">log out</a>){% else %} (<a href="/accounts/signin">sign in</a> | <a href="/accounts/signup">register</a>){% endif %}</div>
        </div>
        <div id="body">

            <div id="linkbar">
                <a href="#">Scoreboard</a> | 
                <a href="{% url teams.views.homePage %}">Rules/Info</a> |
                {% if user.is_authenticated %}
                    <a href="#">Submissions</a> | 
                    <a href="{% url userena.views.profile_detail user.username %}">Team Profile</a>
                {% else %}
                    <a href="{% url userena.views.signin %}">Sign In</a> |
                    <a href="{% url userena.views.signup %}">Register</a>
                {% endif %}
            </div>

            {% block content %}{% endblock %}
        </div>
    </div>    

</body>
</html>
