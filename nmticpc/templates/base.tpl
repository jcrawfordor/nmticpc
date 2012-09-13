<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
    <title>{{ title }} -- NMT ICPC Practice</title>
    <script type="text/javascript" src="/static/timer.js"></script>
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
                <a href="{% url teams.views.scoreboard %}">Scoreboard</a> | 
                <a href="{% url teams.views.homePage %}">Rules/Info</a> |
                {% if user.is_authenticated %}
                    <a href="{% url teams.views.submissions %}">Submissions</a> | 
                    <a href="{% url userena.views.profile_detail user.username %}">Team Profile</a>
                {% else %}
                    <a href="{% url userena.views.signin %}">Sign In</a> |
                    <a href="{% url userena.views.signup %}">Register</a>
                {% endif %}
            </div>

            {% block content %}{% endblock %}
            
            {% if timers %}
            <div id="timecontainer">
                <div id="lefttime">
                    <div class="boxtime" id="utimer">
                    </div>
                    <div class="boxcap">
                        Elapsed
                    </div>
                </div>
                <div id="righttime">
                    <div class="boxtime" id="dtimer">
                        <script type="text/javascript">window.onload = CreateTimer("utimer", {{ timeelapsed }}, "dtimer", {{ timeremaining }});</script>
                    </div>
                    <div class="boxcap">
                        Remaining
                    </div>
                </div>
            </div>
            {% else %}
            <h2>The competition is not currently active.</h2>
            {% endif %}
        </div>
    </div>    

</body>
</html>
