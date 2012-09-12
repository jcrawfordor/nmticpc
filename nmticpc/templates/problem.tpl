{% extends "base.tpl" %}

{% block content %}

<h1>Problem {{problem.number}}</h1>
<p>Worth {{problem.value}} point. {{solvedMessage}}</p>


<fieldset>
<legend>Submit</legend>
<form action="{% url teams.views.problem problem.number %}" method="post" enctype="multipart/form-data">
{% csrf_token %}
{{ form.as_p }}
</fieldset>
<input type="submit" value="submit"> {{ flash }}
</form>


<h2>Submission History</h2>
<table class="wide">
<tr>
    <th>Time</th> <th>Status</th> <th>Comment</th>
</tr>
{% for submission in submission_list %}
<tr>
    <td>{{submission.submitted|date:"H:i:s"}}</td> <td>{{submission.status}}</td> <td>{{submission.comment}}</td>
</tr>
{% endfor %}
</table>

{% endblock %}
