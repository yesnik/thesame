# -*- coding:utf-8 -*-
from django.db import models
from django.conf import settings

class Pic(models.Model):
    alt = models.CharField(max_length=100, verbose_name='Атрибут alt', blank=True)
    src = models.ImageField(upload_to='images/pics', verbose_name='Изображение')

    def admin_thumbnail(self):
        return '<img width="100" src="%s" />' % (settings.MEDIA_URL + str(self.src))
    admin_thumbnail.short_description = 'Изображение'
    admin_thumbnail.allow_tags = True

    def __unicode__(self):
        return self.alt

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
