# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Photomodel, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 2
    readonly_fields = ('image_tag',)


class PhotomodelAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'thumbnail')
    search_fields = ('firstname', 'lastname')
    inlines = [PhotoInline]


admin.site.register(Photomodel, PhotomodelAdmin) 