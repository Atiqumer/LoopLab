# backend/events/urls.py

from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    # path is /events/
    path('', views.event_list, name='event_list'), 
]