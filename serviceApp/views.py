from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

# def download(request):
#     html='<html><body>资料下载</body></html>'
#     return HttpResponse(html)
from .models import Doc
from django.core.paginator import Paginator


def download(request):
    submenu = 'download'
    docList = Doc.objects.all().order_by('-publishDate')
    p = Paginator(docList, 3)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        docList = p.page(page)  # 那一页的数据
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
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
        pageData = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }
    return render(
        request, 'docList.html', {
            'active_menu': 'service',  # base.html，服务支持所在li的id号
            'sub_menu': submenu,
            'docList': docList,
            'pageData': pageData,
        })


# def platform(request):
#     html = '<html><body>人脸识别开放平台</body></html>'
#     return HttpResponse(html)
def platform(request):
    submenu = 'platform'
    return render(request, 'platForm.html', {
        'active_menu': 'service',
        'sub_menu': submenu,
    })


def read_file(file_name, size):
    with open(file_name, mode='rb') as fp:
        while True:
            c = fp.read(size)
            if c:
                yield c
            else:
                break


from django.shortcuts import get_object_or_404
from django.http import StreamingHttpResponse  # 用于将文件流发送给浏览器
import os


def getDoc(request, id):
    doc = get_object_or_404(Doc, id=id)
    update_to, filename = str(doc.file).split('/')
    filepath = '%s/media/%s/%s' % (os.getcwd(), update_to, filename)
    response = StreamingHttpResponse(read_file(filepath, 512))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(
        filename)
    return response


import numpy as np  # 矩阵运算
import urllib  # url解析
import json  # json字符串使用
import cv2  # opencv包
import os  # 执行操作系统命令
from django.views.decorators.csrf import csrf_exempt  # 跨站点验证
from django.http import JsonResponse  # json字符串响应

face_detector_path = "serviceApp\\haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(face_detector_path)  # 生成人脸检测器


def read_image(stream=None):  # 基于数据流的图像读取
    if stream is not None:
        data_temp = stream.read()
    img = np.asarray(bytearray(data_temp), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)  # 将参数img解码为OpenCV的图像数据
    return img


@csrf_exempt  # 用于规避跨站点请求攻击，否则无法使用该API
def facedetect(request):  # 人脸检测视图处理函数
    result = {}  # 用于存放最终的返回结果

    if request.method == "POST":  # 规定客户端使用POST上传图片
        if request.FILES.get("image", None) is not None:  # 读取图像
            img = read_image(stream=request.FILES["image"])  # 调用上面的函数，图像数据存放于img中
        else:  # 没有图像
            result.update({
                "#faceNum": -1,
            })
            return JsonResponse(result)

        if img.shape[2] == 3:  # 是彩色图像
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色图像转灰度图像

        # 进行人脸检测，values存放每个检测到的人脸框的坐标值
        values = face_detector.detectMultiScale(img,
                                                scaleFactor=1.1,
                                                minNeighbors=5,
                                                minSize=(30, 30),
                                                flags=cv2.CASCADE_SCALE_IMAGE)

        # 将检测得到的人脸检测关键点坐标封装
        values = [(int(a), int(b), int(a + c), int(b + d))  # 左上角x,y，右下角x,y
                  for (a, b, c, d) in values]  # a,b为左上角x,y,  c为宽，d为高
        result.update({
            "#faceNum": len(values),  # 人脸数
            "faces": values,
        })
    return JsonResponse(result)


import base64


@csrf_exempt
def facedetectDemo(request):
    result = {}

    if request.method == "POST":
        if request.FILES.get('image') is not None:  #
            img = read_image(stream=request.FILES["image"])
        else:
            result["#faceNum"] = -1
            return JsonResponse(default)

        if img.shape[2] == 3:
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色图像转灰度图像
        else:
            imgGray = img

        # 进行人脸检测
        values = face_detector.detectMultiScale(imgGray,
                                                scaleFactor=1.1,
                                                minNeighbors=5,
                                                minSize=(30, 30),
                                                flags=cv2.CASCADE_SCALE_IMAGE)

        # 将检测得到的人脸检测关键点坐标封装
        values = [(int(a), int(b), int(a + c), int(b + d))
                  for (a, b, c, d) in values]

        # 将检测框显示在原图上
        for (w, x, y, z) in values:
            cv2.rectangle(img, (w, x), (y, z), (0, 255, 0), 2)

        retval, buffer_img = cv2.imencode('.jpg', img)  # 在内存中编码为jpg格式
        img64 = base64.b64encode(buffer_img)  # base64编码用于网络传输
        img64 = str(img64, encoding='utf-8')  # bytes转换为str类型
        result["img64"] = img64  # json封装
    return JsonResponse(result)


# from pyquery import PyQuery as pq
#
# newList = MyNew.objects.all().filter(newType=newName).order_by('-publishDate')
# for mynew in newList:
#     html = pq(mynew.description)        # 使用pq方法解析html内容
#     mynew.mytxt = pq(html)('p').text()  # 截取html段落文字

from .models import Doc  # 数据


def search(request):
    keyword = request.GET.get('keyname')
    newList = Doc.objects.filter(title__icontains=keyword)  # 标题中包含指定关键字
    newName = "关于" + "\"" + keyword + "\"" + "的搜索结果"
    return render(request, 'searchDocs.html', {
        'active_menu': 'docs',
        'newName': newName,
        'newList': newList,
    })
