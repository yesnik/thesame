# -*- coding:utf-8 -*-

from django.core.context_processors import request
from articles.models import Article
 
def recent(request):
    articles = Article.objects.order_by('-created')[:3]
    return {'articles_list_recent': articles}