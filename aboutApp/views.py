from django.shortcuts import render
from .models import Award

# Create your views here.
from django.shortcuts import HttpResponse


def survey(request):
    return render(request, 'survey.html', {'active_menu': 'about', 'sub_menu': 'survey'})
    # return render(request, 'survey.html', {'active_menu':'about'})
    # html='<html><body>企业概况</body></html>'
    # return HttpResponse(html)


def honor(request):
    awards = Award.objects.all()
    return render(request, 'honor.html', {
        'active_menu': 'about',
        'sub_menu': 'honor',
        'awards': awards,
    })
    # return render(request, 'honor.html.', {'active_menu': 'about', 'sub_menu': 'honor'})
    # return render(request, 'honor.html', {'active_menu': 'about'})
    # html='<html><body>荣誉资质</body></html'
    # return HttpResponse(html)
