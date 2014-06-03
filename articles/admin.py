# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('category', 'author', )

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Article, ArticleAdmin) 
admin.site.register(Category, CategoryAdmin) 
