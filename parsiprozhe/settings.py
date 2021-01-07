import os
from django.core.exceptions import ImproperlyConfigured
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

secret = json.load(open(os.path.join(BASE_DIR, 'secret.json')))
secret_dev = json.load(open(os.path.join(BASE_DIR, 'secret_dev.json')))

def get_secret(setting, secrets=secret, secrets_dev=secret_dev):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        if DEBUG:
            return secrets_dev[setting]
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))

SECRET_KEY = get_secret('SECRET_KEY')

DEFAULT_CHARSET = 'utf-8'

FILE_UPLOAD_MAX_MEMORY_SIZE = 15242880

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'category',
    'mptt',
    'shop',
    'ckeditor',
    'logger',
    'contact',
    'googlesearch'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'parsiprozhe.urls'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/registration/login/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shop.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'parsiprozhe.wsgi.application'

DATABASES = {
     'default': {
        'ENGINE': 'mysql.connector.django',
        'OPTIONS': {'charset': 'utf8mb4'},
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('DB_USERNAME'),
        'PASSWORD': get_secret('DB_PASSWORD')
    }
}


AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    }
]


LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


STATICFILES_DIRS = [
    BASE_DIR + "/assets",
    ]

if DEBUG:
    STATICFILES_DIRS.append(os.path.join(BASE_DIR, 'static'))

CART_SESSION_ID = 'cart'

MERCHANT = get_secret('MERCHANT')

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}


'''
INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda x: True
}
'''
SITE_ID = 1