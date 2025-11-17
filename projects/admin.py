# Register your models here.
# backend/projects/admin.py

from django.contrib import admin
from .models import Project 

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_created')
    list_filter = ('category', 'date_created')
    search_fields = ('title', 'description', 'tagline')
    # This will show the contributors list in the admin interface
    filter_horizontal = ('contributors',)