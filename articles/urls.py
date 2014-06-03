# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url

# Импортируем классы для отображения записей.
# Это так называемые class based generic views
from django.views.generic import DetailView, ListView

# Пока мы этот класс представления не создали, но создадим позже
from .views import ArticleListView, ArticleDetailView, ArticleCategoryListView

urlpatterns = patterns('',

    # Показываем список всех статей
    url(r'^$', ArticleListView.as_view(), 
        name="article_list"
    ),

    # Показываем детально статью
    url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), 
        name="article_detail"
    ),

    # Показываем список всех статей категории
    url(r'^(?P<slug>\w+)/$', ArticleCategoryListView.as_view(), 
        name="article_category_list"
    ),
    
)