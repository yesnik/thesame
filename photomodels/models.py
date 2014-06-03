# -*- coding:utf-8 -*-
from django.db import models
from datetime import datetime
from django.conf import settings


def tuplify(x):
    return (str(x), str(x))

current_year = datetime.now().year
YEARS = map(tuplify, range(1980, current_year))


class Photomodel(models.Model):
    """Фотомодель"""
    firstname = models.CharField(max_length=100, verbose_name='Имя')
    lastname = models.CharField(max_length=100, verbose_name='Фамилия')
    description = models.TextField(verbose_name='Описание')

    def thumbnail(self):
        photo = Photo.objects.filter(photomodel=self)[0]
        if photo:
            return u'<img height="100px" src="%s" />' % (settings.MEDIA_URL + str(photo.image))
        else:
            return ''
    thumbnail.short_description = 'Фотография'
    thumbnail.allow_tags = True

    def __unicode__(self):
        return u'{} {}'.format(self.firstname, self.lastname)

    class Meta:
        verbose_name = 'Фотомодель'
        verbose_name_plural = 'Фотомодели'


class Photo(models.Model):
    """Фотографии фотомодели"""
    image = models.ImageField(upload_to='images/photomodels', verbose_name='Изображение')
    photomodel = models.ForeignKey(Photomodel, verbose_name='Фотомодель')

    def image_tag(self):
        return u'<img height="100px" src="%s" />' % (settings.MEDIA_URL + str(self.image))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __unicode__(self):
        return self.image

    class Meta:
        verbose_name = 'Фотография фотомодели'
        verbose_name_plural = 'Фотографии фотомодели'