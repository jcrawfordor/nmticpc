# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

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
        validsubmissions = Submission.objects.filter(problem__number=problem.number,author__user=request.user,valid=True)
        if len(validsubmissions) > 0:
            problem.done = ' problemsolved'
        else:
            problem.done = ''

    c = RequestContext(request, {'problem_list': problemset})
    return render_to_response('submissions.tpl', c)

@login_required
def problem(request, pnum):
    # lists submission history for a specific problem, gives form to submit solution

    thisproblem = Problem.objects.filter(number=pnum)

    # now we get the submissions....
    submissionset = Submission.objects.filter(problem=thisproblem,author__user=request.user).order_by('submitted').reverse()

    # process boolean flags in to a nice status message
    for sub in submissionset:
        if sub.reviewed and sub.valid:
            sub.status = "Accepted, point awarded."
            solvedMessage = "You've solved this problem."
        elif sub.reviewed:
            sub.status = "Rejected, see comments."
        else:
            sub.status = "In queue for review."
    
    c = RequestContext(request, {'problem': thisproblem[0], 'submission_list': submissionset, 'solvedMessage': solvedMessage}) 
    return render_to_response('problem.tpl', c)
