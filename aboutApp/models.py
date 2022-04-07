from django.db import models


# Create your models here.

class Award(models.Model):  # 荣誉模型
    # description = models.TextField(max_length=500, blank=True,
    #                                null=True)  # 文字描述
    # photo = m0odels.ImageField(upload_to='Award/', blank=True)  # 图片
    description = models.TextField(max_length=500, blank=True,
                                   null=True, verbose_name='荣誉描述')  # 文字描述
    photo = models.ImageField(upload_to='Award/', blank=True
                              , verbose_name='荣誉照片')  # 图片


class Meta:
    verbose_name = '获奖和荣誉'  # 为模型定义别名
    verbose_name_plural = '获奖和荣誉'  # 别名的复数形式
