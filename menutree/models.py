# -*- coding:utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Menu(models.Model):
    name = models.CharField(u'Имя', max_length=50, unique=True)
    slug = models.SlugField(u'Алиас')
    description = models.TextField(u'Описание', blank=True, null=True)

    class Meta:
        verbose_name = u'Меню'
        verbose_name_plural = u'Меню'

    def __unicode__(self):
        return u"%s" % self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class MenuItem(MPTTModel):
    menu = models.ForeignKey(
        Menu,
        verbose_name=u'Меню'
        )

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u'Родительский пункт меню')

    order = models.IntegerField(
        u'Сортировка',
        default=500
        )

    link_url = models.CharField(
        u'URL',
        max_length=100,
        help_text=u'URL контента, к примеру, /about/ or http://foo.com/'
        )

    title = models.CharField(
        u'Поле title',
        max_length=100
        )
         

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __unicode__(self):
        return self.title