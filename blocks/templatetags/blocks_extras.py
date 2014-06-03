# -*- coding:utf-8 -*-
from django import template
from blocks.models import Block

register = template.Library()
 
@register.inclusion_tag('blocks/inc/block.html')
def show_block(slug):
    """Отображение на странице статических элементов по их slug"""
    try:
        block = Block.objects.get(slug=slug)
    except (Block.DoesNotExist):
        raise template.TemplateSyntaxError("%r tag requires correct 'slug' parameter" % __name__)
    return {'block': block}