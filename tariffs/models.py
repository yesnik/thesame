# -*- coding:utf-8 -*-
from django.db import models

class Tariff(models.Model):
    """Блок тарифов на главной странице сайта"""
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='Идентификатор')
    price = models.CharField(max_length=100, verbose_name='Цена')
    content = models.TextField(verbose_name='Описание')
    is_best = models.BooleanField(verbose_name="Лучшее предложение")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'