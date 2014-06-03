# -*- coding:utf-8 -*-
from django.db import models

class Block(models.Model):
    """Статические блоки информации на страницах сайта"""
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='Идентификатор')
    content = models.TextField(verbose_name='Содержимое')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'
