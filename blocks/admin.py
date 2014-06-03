from django.contrib import admin
from .models import Block

class BlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ['title', 'slug']

admin.site.register(Block, BlockAdmin) 