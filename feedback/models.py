# -*- coding:utf-8 -*-
from django.db import models

class Feedback(models.Model):
    subject = models.CharField(u'Тема', max_length=100)
    email = models.EmailField(u'Email', blank=True)
    message = models.TextField(u'Сообщение')
    added = models.DateTimeField(u'Создано', auto_now_add=True)

    def __unicode__(self):
        return self.subject

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
