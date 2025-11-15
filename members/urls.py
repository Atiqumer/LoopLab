# members/urls.py

from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    # path is /contributors/
    path('', views.contributor_list, name='contributor_list'), 
]