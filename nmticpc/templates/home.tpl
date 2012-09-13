{% extends "base.tpl" %}

{% block content %}

<h1>Rules</h1>
<h2>Time, Problems</h2>
<p>Six problems will be distributed, and teams will be allowed 2.5 hours to solve as many as they can. Problems may be solved in any order. Problems can be submitted an unlimited number of times until their solution is correct (although see scoring for a caveat). This scoring software will automatically open and close submissions at the beginning and end of the competition.</p>
<h2>Scoring</h2>
<p>Each problem is worth one point, and the team with the most points will win. In case of a tie, the tied teams will have a "total competion time" calculated by taking the sum of the time from the beginning of the competition to the submission time of a correct solution for each problem, plus a 20 minute penalty for each incorrect submission. The team with the smaller total competition time will then be ranked higher.</p>
<p>When each problem is submitted it will be enqueued. The judge will test the problem as quickly as possible, and then either accept or reject your solution. If your solution is rejected, a comment will be provided explaining why. Feel free to ask the judge questions about a rejection.</p>
<h2>Language</h2>
<p>We don't yet know what programming languages the regional competition will allow, but Java, C, and C++ are a sure bet. For this practice competition, feel free to use Python or PHP. If you would like to use a different language, speak with the judge in advance so that he can set up an environment for that language on his testing machine.</p>

{% endblock %}
