# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import FeedbackCreate, FeedbackSuccess

urlpatterns = [
    url(r'^create/$', FeedbackCreate.as_view(), name='create'),
    url(r'^success/$', FeedbackSuccess.as_view(), name='success'),
    #url(r'^(?P<pk>[0-9]+)/$', AuthorUpdate.as_view(), name='author_update'),
    #url(r'^(?P<pk>[0-9]+)/delete/$', AuthorDelete.as_view(), name='author_delete'),
]