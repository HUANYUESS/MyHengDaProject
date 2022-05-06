from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

def contact(request):
    return render(request, 'contact.html', { #欢迎咨询
        'active_menu': 'contactus',  #base.html中人才招聘所在li的id号为contactus
        'sub_menu': 'contact',
    })

from .models import Ad
from .forms import ResumeForm

def recruit(request):
    AdList = Ad.objects.all().order_by('-publishDate')
    if request.method == 'POST':
        resumeForm = ResumeForm(data=request.POST, files=request.FILES) #创建模型表单对象
        if resumeForm.is_valid():
            resumeForm.save() #存到数据库
            return render(request, 'success.html', {  #提交了简历，进入success页面
                'active_menu': 'contactus',
                'sub_menu': 'recruit',
            })
    else:  #没有提交
        resumeForm = ResumeForm()  #创建模型表单对象，并传给recruit.html
    return render(
        request, 'recruit.html', {
            'active_menu': 'contactus',
            'sub_menu': 'recruit',
            'AdList': AdList,
            'resumeForm': resumeForm,
        })


# def recruit(request):
#     AdList = Ad.objects.all().order_by('-publishDate')
#     return render(
#         request, 'recruit.html', {
#             'active_menu': 'contactus',
#             'sub_menu': 'recruit',
#             'AdList': AdList,
#         })


# def recruit(request):
#     return render(
#         request, 'recruit.html', {  #加入恒达
#             'active_menu': 'contactus',
#             'sub_menu': 'recruit',
#     })


# def contact(request):
#     html='<html><body>欢迎咨询</body></html>'
#     return HttpResponse(html)
#
#
# def recruit(request):
#     html = '<html><body>加入恒达</body></html>'
#     return HttpResponse(html)
