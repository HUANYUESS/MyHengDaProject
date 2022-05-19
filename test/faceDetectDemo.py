import cv2, requests
url = "http://localhost:8000/serviceApp/facedetect/"  # 开发阶段的后台服务器(http://localhost:8000)+应用名+访问接口（facedetect）

# 上传图像并检测
tracker = None
imgPath = "face.jpg"  #图像路径
files = {
    "image": ("filename2", open(imgPath, "rb"), "image/jpeg"), #open函数读取图片，封装在files变量中
}

req = requests.post(url, data=tracker, files=files).json() #requests.post发送请求，返回的数据转换为json字符串
print("获取信息: {}".format(req)) #控制台打印字符串内容

# 将检测结果框显示在图像上
img = cv2.imread(imgPath)
for (w, x, y, z) in req["faces"]: # w,x左上角，  y,z右下角
    cv2.rectangle(img, (w, x), (y, z), (0, 255, 0), 2)  #绿色框，粗细为2

cv2.imshow("face detection", img)  #有标题栏
cv2.waitKey(0)
