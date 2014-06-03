# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url

# Импортируем классы для отображения записей.
# Это так называемые class based generic views
from django.views.generic import DetailView, ListView

from .views import PageListView, PageDetailView

urlpatterns = patterns('',

    # Показываем список всех статей
    url(r'^$', PageListView.as_view(), 
        name="page_list"
    ),

    # Показываем детально статью
    url(r'^(?P<pk>[0-9]+)/$', PageDetailView.as_view(), 
        name="page_detail_id"
    ),

    # Показываем детально статью
    url(r'^(?P<slug>\w+)/$', PageDetailView.as_view(), 
        name="page_detail"
    ),

)