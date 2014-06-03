# -*- coding:utf-8 -*-
from django.db import models

class Photographer(models.Model):
    """Фотограф"""
    firstname = models.CharField(max_length=100, verbose_name='Имя')
    lastname = models.CharField(max_length=100, verbose_name='Фамилия')
    about = models.TextField(verbose_name='О себе')

    def __unicode__(self):
        return u'{} {}'.format(self.firstname, self.lastname)

    class Meta:
        verbose_name = 'Фотограф'
        verbose_name_plural = 'Фотографы'
