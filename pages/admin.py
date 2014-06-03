from django.contrib import admin

from .models import Page, Category

class PageAdmin(admin.ModelAdmin):
    filter_horizontal = ('category', )
    list_display = ('title', 'slug', )

admin.site.register(Page, PageAdmin) 
admin.site.register(Category) 

