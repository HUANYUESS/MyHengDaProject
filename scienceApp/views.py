from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse


def science(request):
    return render(request, 'science.html', {'active_menu': 'science'})
    # return render(request, 'science.html')

