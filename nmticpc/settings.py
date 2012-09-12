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
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django',          # Or path to database file if using sqlite3.
        'USER': 'icpc',                      # Not used with sqlite3.
        'PASSWORD': 'TEhkEkXEGC5423',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/var/www-icpc/media/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = ('/var/www-icpc/nmticpc/style',)
STATIC_ROOT = "/var/www-icpc/static"
STATIC_URL = "/static/"

# Make this unique, and don't share it with anybody.
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
    'teams',
)

# Userena stuff
ANONYMOUS_USER_ID = -1
LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
USERENA_ACTIVATION_REQUIRED = False

# model for user info
AUTH_PROFILE_MODULE = 'teams.TeamProfile'
