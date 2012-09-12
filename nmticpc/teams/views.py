# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from teams.models import Problem

def homePage(request):
    # kind of a stub view, but we need it rather than just using staticpage
    # because this template gets info from context processors.
    c = RequestContext(request)
    return render_to_response('home.tpl', c)

@login_required
def submissions(request):
    # Lists problems open, problem status, link to submission attempts
    problemset = Problem.objects.order_by('number')

    c = RequestContext(request, {'problem_list': problemset})
    return render_to_response('submissions.tpl', c)
