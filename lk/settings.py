"""
Django settings for lk project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

ADMINS = [('Admin', 'lksunc@gmail.com'), ('Tatiana', 'unforgiven8@yandex.ru')]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(z^g_8g(b&dlno6_xt309=gg!$kw5e@3m_cp#q+k1_ux$t65d1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.213.247.155.130', '.lk.internat.msu.ru']

ACCOUNT_ACTIVATION_DAYS = 2 

#EMAIL_HOST = 'automail.aesc.msu.ru'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'auto'
#EMAIL_HOST_PASSWORD = 'wzhuI9vS3h'
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'auto@automail.aesc.msu.ru'

#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'auto'
#EMAIL_HOST_PASSWORD = '2g27fg237gfiq3gfig'
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'lk@internat.msu.ru'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'lksunc@gmail.com'
EMAIL_HOST_PASSWORD = 'rhtvtyxeucrfz11'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'lksunc@gmail.com'

#EMAIL_HOST = 'smtp.yandex.ru'
#EMAIL_PORT = 465
#EMAIL_HOST_USER = 'tgolubkova007@yandex.ru'
#EMAIL_HOST_PASSWORD = ',f[xbcfhfq28'
#EMAIL_USE_SSL = True
#DEFAULT_FROM_EMAIL = 'tgolubkova007@yandex.ru'

# Application definition

INSTALLED_APPS = (
    'lkforms',
    'lkregistration',
    'lkforum',
    'lkmoderation',
    'lktest',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lk.urls'

WSGI_APPLICATION = 'lk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'lksunc',                      
        'USER': 'webmaster',                     
        'PASSWORD': 'bnmKLop',                  
        'HOST': '',                      
        'PORT': '',                      
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
)

LOCALE_PATHS = [
    '/var/www/lk/locale',
]

TIME_ZONE = 'Europe/Minsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/var/www/lk/allstatic'

#STATICFILES_DIRS = (
#    '',
#)

TEMPLATE_DIRS = (
    '/var/www/lk/templates', # Change this to your own directory.
)

TEMPLATE_CONTEXT_PROCESSORS = (
     'django.contrib.auth.context_processors.auth',
     'django.core.context_processors.request',
     )

#AUTH_PROFILE_MODULE = 'forms.UserProfile'

MEDIA_ROOT = '/var/www/lk/media'
MEDIA_URL = ''

