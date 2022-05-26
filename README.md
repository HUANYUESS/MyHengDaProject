# 项目运行命令
    python manage.py runserver

# 实验环境:
> Python: 3.8 【必须】(如果用低版本会报奇奇怪怪的包不错误)
> Whoosh
> opencv-python
> django-haystack
> lxml
> docxtpl
> Django
> urllib3
> sqlparse
> 
# Week14_新增内容:
> 新增主页模块

> 新增主页缓存(在views的home函数中进行设置)

**具体包含**
- (1)轮播横幅
- (2)企业概况
- (3)新闻动态
- (4)通知公告
- (5)科研基地
- (6)联系我们
- (7)产品中心


# Week13_新增内容:
> 新增服务支持模块，资料下载和AI人脸识别，并补充搜索框选项。

# Week12_新增内容:
> 新增人才招聘模块
>> 嵌入百度地图
>> 发送邮件
>>> 邮箱信息设置可在MyHengDaProject的setting文件中进行设置
>> 动态生成word文档

# Week11_新增内容:
> 新增新闻模块
>> 开发'新闻列表'和'新闻详情'页面
>> 新闻搜索


# Week9_新增内容:
> 新增产品中心模块
> 制作产品列表页面
> Django分页显示
> 制作产品详情页面


# Week8_新增内容:
> 新增公司简介模块
> 制作侧边导航栏
> 数据库模型
> 优化后台管理

# Week7_新增内容:
> 新增产品中心页面模块

# Week6_新增内容:
> 新增数据库超级用户
>> 账号: pythonweb
>> 密码: 123

> 新增公司简介页面模块，aboutApp目录下的文件

# Week5_新增内容:
    新增科研基地界面
    新增页面模板

## 二级路由
    各路由对应的访问网址：
        (1)首页：http://127.0.0.1:8000/
        (2)企业概况：http://127.0.0.1:8000/aboutApp/survey/
        (3)荣誉资质：http://127.0.0.1:8000/aboutApp/honor/
        (4)欢迎咨询：http://127.0.0.1:8000/contactApp/contact/
        (5)加入恒达：http://127.0.0.1:8000/contactApp/recruit/
        (6)公司要闻：http://127.0.0.1:8000/newsApp/company/
        (7)行业新闻：http://127.0.0.1:8000/newsApp/industry/
        (8)通知公告：http://127.0.0.1:8000/newsApp/notice/
        (9)家用机器人：http://127.0.0.1:8000/productsApp/robot/
        (10)智能监控：http://127.0.0.1:8000/productsApp/monitoring/
        (11)人脸识别解决方案：http://127.0.0.1:8000/productsApp/face/
        (12)资料下载：http://127.0.0.1:8000/serviceApp/download/
        (13)人脸识别开放平台：http://127.0.0.1:8000/serviceApp/platform/
        (14)科研基地：http://127.0.0.1:8000/scienceApp/science/

