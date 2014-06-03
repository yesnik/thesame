# -*- coding:utf-8 -*-
from django.db import models
from django.conf import settings

class Slide(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', blank=True)
    image = models.ImageField(upload_to='images/slides', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', blank=True)

    def admin_thumbnail(self):
        if not self.image:
            return ''
        return '<img width="100" src="%s" />' % (settings.MEDIA_URL + str(self.image ))
    admin_thumbnail.short_description = 'Изображение'
    admin_thumbnail.allow_tags = True

    def __unicode__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
