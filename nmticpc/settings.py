# Django settings for nmticpc project.

import os
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'icpc',
        'PASSWORD': 'TEhkEkXEGC5423',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Denver'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# don't load i18n libs to save time, we don't use them anyway
USE_I18N = False
USE_L10N = False

# Media locations
MEDIA_ROOT = '/var/www-icpc/media/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = ('/var/www-icpc/nmticpc/style',)
STATIC_ROOT = "/var/www-icpc/static"
STATIC_URL = "/static/"

SECRET_KEY = '2oqtq=_@xc1+gix@2w+3q%mr^*vd$!)8ormh28x70qujua70)h'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                )

AUTHENTICATION_BACKENDS = (
                'userena.backends.UserenaAuthenticationBackend',
                'guardian.backends.ObjectPermissionBackend',
                'django.contrib.auth.backends.ModelBackend',
                )

MIDDLEWARE_CLASSES = (
                'django.middleware.common.CommonMiddleware',
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
                )

ROOT_URLCONF = 'nmticpc.urls'

TEMPLATE_DIRS = (
                    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
                )

INSTALLED_APPS = (
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.sites',
                'django.contrib.messages',
                'django.contrib.admin',
                'django.contrib.staticfiles',
                'userena',
                'guardian',
                'easy_thumbnails',
                'nmticpc.teams',
)

# Userena stuff
ANONYMOUS_USER_ID = -1
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
USERENA_ACTIVATION_REQUIRED = False

# model for user info
AUTH_PROFILE_MODULE = 'teams.TeamProfile'
