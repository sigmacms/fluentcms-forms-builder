"""
Django settings for example project.

Generated by 'django-admin startproject' using Django 1.11.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os, re

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'YOUR_SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SERVE_MEDIA = True

ALLOWED_HOSTS = []

# Application definition

PROJECT_APPS = [
    'fluentcms_forms_builder',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'fluent_pages',
    'fluent_pages.pagetypes.fluentpage',

    'mptt',
    'polymorphic',
    'polymorphic_tree',
    'parler',
    'slug_preview',
    
    'fluent_contents',
    'fluent_contents.plugins.text',

    'any_urlfield',
    'django_wysiwyg',
    'tinymce',

    'forms_builder.forms',
] + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'fluent_contents.middleware.HttpRedirectRequestMiddleware',
]

ROOT_URLCONF = 'example.urls'

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(__file__), 'templates'),
            os.path.join(os.path.dirname(__file__), 'templates', 'layouts'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'example.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')

STATIC_URL = '/static/'

CSRF_COOKIE_DOMAIN = None

FLUENT_PAGES_TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates', 'layouts')

DJANGO_WYSIWYG_FLAVOR = "tinymce"
