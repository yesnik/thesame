# -*- coding:utf-8 -*-
from django import template
from tariffs.models import Tariff

register = template.Library()
 
@register.inclusion_tag('tariffs/inc/tariff.html')
def show_tariff(tariff):
    """Отображение на странице тарифа"""
    return {'tariff': tariff}