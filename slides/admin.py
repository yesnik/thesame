# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Slide

class SlideAdmin(admin.ModelAdmin):
    list_display = ('admin_thumbnail', 'description')
    search_fields = ('image', 'description')

admin.site.register(Slide, SlideAdmin) 
