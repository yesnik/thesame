from django.contrib import admin
from .models import Pic

class AdminPic(admin.ModelAdmin):
    list_display = ('admin_thumbnail', 'alt')
    search_fields = ('alt', 'src')

admin.site.register(Pic, AdminPic) 

