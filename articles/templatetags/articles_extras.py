# -*- coding:utf-8 -*-
from django import template
from articles.models import Article

register = template.Library()
 
@register.inclusion_tag('articles/inc/article_short.html')
def article_short(article):
    """Отобразить анонс статьи для списка статей"""
    return {'article': article}


@register.inclusion_tag('articles/inc/article_recent.html')
def article_recent(article):
    """Отобразить новость списка в блоке Последние новости"""
    return {'article': article}