# -*- coding:utf-8 -*-
from django.contrib import admin

from .models import Work, Photo, Category

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 2
    readonly_fields = ('image_tag',)

class WorkAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description', 'description_short', 'client')
    filter_horizontal = ('photomodel', 'photographer', 'category')
    inlines = [PhotoInline]
    list_display = ('title', 'admin_thumbnail')

admin.site.register(Work, WorkAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug')

admin.site.register(Category, CategoryAdmin)
