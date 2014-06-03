# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Photographer

class PhotographAdmin(admin.ModelAdmin):
    search_fields = ('firstname', 'lastname')


admin.site.register(Photographer, PhotographAdmin) 
