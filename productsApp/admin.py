from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, ProductImg

# admin.site.register(Product)
# admin.site.register(ProductImg)


class ProductImgInline(admin.StackedInline):  # 内联模型管理器
    model = ProductImg  # 以集成方式在后台显示
    extra = 1  # 默认显示条目的数量


class ProductAdmin(admin.ModelAdmin):  # 产品模型管理器
    inlines = [ProductImgInline, ]  # 内联属性


admin.site.register(Product, ProductAdmin)  # 绑定产品模型和产品模型管理器
