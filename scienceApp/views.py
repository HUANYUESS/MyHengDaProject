from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse


def science(request):
    html='<html><body>科研基地</body></html>'
    return HttpResponse(html)
