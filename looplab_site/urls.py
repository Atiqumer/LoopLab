"""
URL configuration for looplab_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings 
import os
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('contributors/', include('members.urls')),
    path('projects/', include('projects.urls')),
    path('events/', include('events.urls')),
    path('contact/', include('contact.urls')),
]

if settings.DEBUG:
    # Use settings.BASE_DIR.parent to match the definition in settings.py
    # Although this argument is usually ignored when STATICFILES_DIRS is set, 
    # it is the standard way to ensure serving in development.
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR.parent, 'static'))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)