# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm

from teams.models import Problem
from teams.models import Submission

def homePage(request):
    # kind of a stub view, but we need it rather than just using staticpage
    # because this template gets info from context processors.
    c = RequestContext(request)
    return render_to_response('home.tpl', c)

@login_required
def submissions(request):
    # Lists problems open, problem status, link to submission attempts
    problemset = Problem.objects.order_by('number')

    # find out if the user has already solved this problem, if so set a class name
    for problem in problemset:
        if problem.isSolvedBy(request.user):
            problem.done = ' problemsolved'
        else:
            problem.done = ''
        
    c = RequestContext(request, {'problem_list': problemset})
    return render_to_response('submissions.tpl', c)

from teams.models import Submission
# form class for submissions
class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ('content',)

@login_required
def problem(request, pnum):

    # lists submission history for a specific problem, gives form to submit solution
    thisproblem = Problem.objects.filter(number=pnum)

    # Process form first, so that the list will be right if they just submitted
    flash = ""
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():  
            newSubmission = form.save(commit=False)
            newSubmission.author = request.user
            newSubmission.problem = thisproblem[0]
            newSubmission.reviewed = False
            newSubmission.valid = False
            newSubmission.save()
            flash = "Submission received."
    else:
        form = SubmissionForm()

    # now we get the submissions....
    submissionset = Submission.objects.filter(problem=thisproblem,author=request.user).order_by('submitted').reverse()

    solved = False

    # process boolean flags in to a nice status message
    for sub in submissionset:
        if sub.reviewed and sub.valid:
            sub.status = "Accepted, point awarded."
            solved = True
        elif sub.reviewed:
            sub.status = "Rejected, see comments."
        else:
            sub.status = "In queue for review."

    c = RequestContext(request, {'problem': thisproblem[0], 'submission_list': submissionset, 'solved': solved, 'form': form, 'flash': flash}) 
    return render_to_response('problem.tpl', c)

from util import getRankedTeams
def scoreboard(request):
    scoreboard = getRankedTeams()
    c = RequestContext(request, {'teamlist': scoreboard})
    return render_to_response('scoreboard.tpl', c)
