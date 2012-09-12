from django.contrib import admin
from nmticpc.teams.models import TeamProfile, Problem, Submission

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('number', 'value')

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('author', 'problem', 'reviewed', 'valid')
    list_filter = ('reviewed', 'valid')

# admin.site.register(TeamProfile) #Already registered....?
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Submission, SubmissionAdmin)
