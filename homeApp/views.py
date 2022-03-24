from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse


def home(request):
    return render(request, 'home.html')
    # html = '<html><body>首页</body></html>'
    # return HttpResponse(html)