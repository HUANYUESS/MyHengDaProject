from django.contrib import admin

# Register your models here.
from .models import Award

class AwardAdmin(admin.ModelAdmin):
    list_display = ['description','photo']

admin.site.register(Award, AwardAdmin)
