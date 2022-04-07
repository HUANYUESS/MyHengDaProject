from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

from .models import Product

# 三合一 + 模型数据过滤、排序和渲染
def products(request,productName):
    submenu=productName  #侧边导航栏的激活状态
    if productName=='robot':
        productName='家用机器人'
    elif productName=='monitor':
        productName='智能监控'
    else:
        productName='人脸识别解决方案'

    productList = Product.objects.all().filter(
        productType=productName).order_by('-publishDate')

    return render(request,'productList.html',{
        'active_menu':'products',
        'sub_menu':submenu,
        'productName':productName,
        'productList':productList,   #给四个模板变量传值
    })



# 三合一
# def products(request,productName):
#     submenu=productName  #侧边导航栏的激活状态
#     if productName=='robot':
#         productName='家用机器人'
#     elif productName=='monitor':
#         productName='智能监控'
#     else:
#         productName='人脸识别解决方案'
#
#     return render(request,'productList.html',{
#         'active_menu':'products',
#         'sub_menu':submenu,
#         'productName':productName,  #给三个模板变量传值
#     })


# def robot(request):
#     html='<html><body>家用机器人</body></html>'
#     return HttpResponse(html)


# def monitoring(request):
#     html = '<html><body>智能监控</body></html>'
#     return HttpResponse(html)


# def face(request):
#     html = '<html><body>人脸识别解决方案</body></html>'
#     return HttpResponse(html)
