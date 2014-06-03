# -*- coding:utf-8 -*-
from django.db import models
from django.conf import settings

class PhotoAbstract(models.Model):
    image = models.ImageField(upload_to='images/photomodels', verbose_name='Изображение')
    
    def image_tag(self):
        if not self.image:
            return ''
        return u'<img height="100px" src="%s" />' % (settings.MEDIA_URL + str(self.image))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __unicode__(self):
        return self.image
        
    class Meta:
        abstract = True