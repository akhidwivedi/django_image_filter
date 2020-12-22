from django.contrib import admin
from .models import Image
from .models import Category

# Register your models here.


class AdminImage(admin.ModelAdmin):
    list_display = ['title','picture','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Image,AdminImage)
admin.site.register(Category,AdminCategory)
