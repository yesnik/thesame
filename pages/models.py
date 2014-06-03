# -*- coding:utf-8 -*-
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='Идентификатор')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='Идентификатор')
    content = models.TextField(verbose_name='Содержание')
    category = models.ManyToManyField(Category, verbose_name=u'Категория')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

