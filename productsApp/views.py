from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

from .models import Product

from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404


def productDetail(request,id):
    product=get_object_or_404(Product,id=id)
    product.views+=1
    product.save()
    return render(request,'productDetail.html',{
        'active_menu':'products',
        'product':product, #传递给前端的模板变量
    })




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



    # 在获得了过滤的数据（productList）之后，添加如下代码
    p = Paginator(productList, 2)  # 过滤好的数据，每页显示两条
    if p.num_pages <= 1:
        pageData = ''  # 向前端传递空串
    else:
        page = int(request.GET.get('page', 1))  # 前端页码超链接 传过来的具体页码
        productList = p.page(page)  # 具体页码要显示的两条记录
        left = []  # 列表
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages  # 总页数
        page_range = p.page_range  # 页数范围
        if page == 1:
            right = page_range[page:page + 2]  # 列表 right[0]=2 right[1]=3
            print(total_pages)
            if right[-1] < total_pages - 1:  # right[-1]为3
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]  # 倒数第3页，倒数第2页
            if left[0] > 2:  # 倒数第3页页码大于2
                left_has_more = True
            if left[0] > 1:
                first = True
        else:  # 不是第一页或最后一页
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            right = page_range[page:page + 2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        pageData = {  # 字典，会传给前端
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }
    # Week 8
    # 分页版本的 render
    return render(request, 'productList.html', {
        'active_menu': 'products',
        'sub_menu': submenu,
        'productName': productName,
        'productList': productList,
        'pageData': pageData,
    })

    # Week 7
    # return render(request,'productList.html',{
    #     'active_menu':'products',
    #     'sub_menu':submenu,
    #     'productName':productName,
    #     'productList':productList,   #给四个模板变量传值
    # })



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
