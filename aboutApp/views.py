from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse


def survey(request):
    html='<html><body>企业概况</body></html>'
    return HttpResponse(html)


def honor(request):
    html='<html><body>荣誉资质</body></html'
    return HttpResponse(html)
