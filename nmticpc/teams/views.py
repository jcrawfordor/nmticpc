# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

def homePage(request):
    return render_to_response('simplecontent.tpl', {'theContent': "This is the homepage"})
