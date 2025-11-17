# backend/projects/urls.py

from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # path is /projects/
    path('', views.project_list, name='project_list'), 
]