from django.contrib import admin

# Register your models here.
# members/admin.py
from django.contrib import admin
from .models import Contributor 

@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'profile_photo') 
    search_fields = ('name', 'bio')