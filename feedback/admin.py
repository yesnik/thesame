from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'message', 'added')
    search_fields = ['subject', 'message', 'email']

admin.site.register(Feedback, FeedbackAdmin) 
