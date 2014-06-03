# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Tariff


class TariffAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_best')
    search_fields = ['title', 'slug']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Tariff, TariffAdmin) 
