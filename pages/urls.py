# pages/urls.py

from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    # This path maps the root URL of this app to the home_page view
    path('', views.home_page, name='home'), 
]