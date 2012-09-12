# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def homePage(request):
    # kind of a stub view, but we need it rather than just using staticpage
    # because this template gets info from context processors.
    c = RequestContext(request)
    return render_to_response('home.tpl', c)
