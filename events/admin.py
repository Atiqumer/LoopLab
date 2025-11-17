# backend/events/admin.py

from django.contrib import admin
from .models import Event 

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_time', 'location', 'is_upcoming')
    list_filter = ('is_upcoming', 'date_time')
    search_fields = ('title', 'description', 'location')