from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse


# def home(request):
#     return render(request, 'home.html', {'active_menu': 'home'})
# return render(request, 'home.html')
# html = '<html><body>首页</body></html>'
# return HttpResponse(html)


# 打开homeApp的views.py，重新编辑home函数
from newsApp.models import MyNew
from django.db.models import Q  # 查询函数

from django.views.decorators.cache import cache_page
@cache_page(60 * 15) # 单位：秒数，这里指缓存 15 分钟
def home(request):
    # 新闻里，不是通知公告的
    newList = MyNew.objects.all().filter(~Q(newType='通知公告')).order_by('-publishDate')
    postList = set()
    postNum = 0
    for s in newList:
        if s.photo:  # 有展报
            postList.add(s)
            postNum += 1
        if postNum == 3:  # 只截取最近的3个展报
            break

    # 新闻列表
    if (len(newList) > 7):
        newList = newList[0:7]  # 7条新闻

    # 通知公告
    noteList = MyNew.objects.all().filter(
        Q(newType='通知公告')).order_by('-publishDate')
    if (len(noteList) > 4):
        noteList = noteList[0:4]

    from productsApp.models import Product
    # 产品中心
    productList = Product.objects.all().order_by('-views')
    if (len(productList) > 4):
        productList = productList[0:4]

    # 返回结果
    return render(request, 'home.html', {
        'active_menu': 'home',
        'postList': postList,
        'newList': newList,
        'noteList': noteList,
        'productList': productList,
    })

