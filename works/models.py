# -*- coding:utf-8 -*-
from django.db import models
from django.conf import settings
from util.photo_abstract import PhotoAbstract


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='Алиас страницы')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория работы'
        verbose_name_plural = 'Категории работ'


class Work(models.Model):
    """Работа, выполненная компанией для заказчика"""
    title = models.CharField(max_length=100, verbose_name='Название')
    client = models.CharField(max_length=255, verbose_name='Заказчик')
    description_short = models.CharField(max_length=255, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Полное описание')
    category = models.ManyToManyField(Category, verbose_name=u'Категории')
    photomodel = models.ManyToManyField('photomodels.Photomodel', verbose_name=u'Фотомодели')
    photographer = models.ManyToManyField('photographers.Photographer', verbose_name=u'Фотографы')

    def admin_thumbnail(self):
        try:
            photo = Photo.objects.filter(works=self)[0]
        except IndexError:
            return ''

        if not photo:
            return ''
        return '<img width="100" src="%s" />' % (settings.MEDIA_URL + str(photo.image))
    admin_thumbnail.short_description = 'Изображение'
    admin_thumbnail.allow_tags = True

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class Photo(PhotoAbstract):
    """Фотографии проекта"""
    
    works = models.ForeignKey(Work, verbose_name='Работа')

    class Meta:
        verbose_name = 'Фотография проекта'
        verbose_name_plural = 'Фотографии проекта'
