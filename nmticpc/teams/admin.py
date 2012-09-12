from django.contrib import admin
from nmticpc.teams.models import TeamProfile, Problem, Submission

# admin.site.register(TeamProfile) #Already registered....?
admin.site.register(Problem)
admin.site.register(Submission)
