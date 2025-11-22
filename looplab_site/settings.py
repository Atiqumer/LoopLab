"""
Django settings for looplab_site project.
"""

import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv 

# Load environment variables from .env file for local development
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR is set up correctly to point to the project root (where manage.py is).
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# SECURITY WARNING: fetch SECRET_KEY from environment
SECRET_KEY = os.getenv('SECRET_KEY', 'default-insecure-key-local-only')

# SECURITY WARNING: don't run with debug turned on in production!
# Reads DEBUG from environment (e.g., DEBUG=False on Railway)
DEBUG = os.getenv('DEBUG', 'True') == 'True' 

# ALLOWED_HOSTS for local (127.0.0.1) and Railway (*)
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Your Apps
    'members',
    'pages',
    'projects',
    'events',
    'contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # ADDED FOR PRODUCTION STATIC SERVING
]

ROOT_URLCONF = 'looplab_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'looplab_site.wsgi.application'


# Database Configuration for Railway (Uses dj-database-url)
DATABASES = {
    'default': dj_database_url.config(
        # Use DATABASE_URL from Railway environment, or fall back to local SQLite
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600 # Recommended for production
    )
}

# settings.py



# Password validation (Standard Django)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization (Standard Django)
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# --- STATIC AND MEDIA FILES CONFIGURATION ---

STATIC_URL = '/static/'

# CRITICAL FIX 1: STATIC_ROOT is where files are collected for WhiteNoise/Production
# This is where collectstatic will copy all files into a 'staticfiles' folder at the root.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

# CRITICAL FIX 2: STATICFILES_DIRS points to the source 'static' folder next to manage.py
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), 
]

# Use WhiteNoise storage for production performance and caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Media settings for user-uploaded files (like contributor photos)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'