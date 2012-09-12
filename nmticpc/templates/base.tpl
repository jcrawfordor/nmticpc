<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
    <title>{{ title }} -- NMT ICPC Practice</title>
    <link rel="stylesheet" type="text/css" href="/static/mainstyle.css">
</head>
<body>
    <div id="container">
        <div id="header">
            NMT ICPC
            <div id="userinfo">{% if user.is_authenticated %} {{ user.username }} (<a href="/accounts/signout">log out</a>){% else %} (<a href="/accounts/signin">sign in</a> | <a href="/accounts/signup">register</a>){% endif %}</div>
        </div>
        <div id="body">
            {% block content %}{% endblock %}
        </div>
    </div>    

</body>
</html>
