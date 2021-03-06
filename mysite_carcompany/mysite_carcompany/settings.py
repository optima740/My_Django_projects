"""
Django settings for mysite_carcompany project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.urls import reverse_lazy
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2$x58x2pqskodxyh6nqa5+8%k1lq-#7@o=-673kp%p^d^4n&j3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

# for GDAL:
"""
import os
if os.name == 'nt':
    import platform
    OSGEO4W = r"/OSGeo4W"
    #if '64' in platform.architecture()[0]:
        #OSGEO4W += "64"
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']
"""

VENV_BASE = os.environ['VIRTUAL_ENV']
os.environ['PATH'] = os.path.join(VENV_BASE, 'Lib/site-packages/osgeo') + ';' + os.environ['PATH']
os.environ['PROJ_LIB'] = os.path.join(VENV_BASE, 'Lib/site-packages/osgeo/data/proj') + ';' + os.environ['PATH']
#GDAL_LIBRARY_PATH = '/Users/Andrey/PycharmProjects/untitled/venv/Lib/site-packages/django/contrib/gis/gdal/libgdal.py'
GEOS_LIBRARY_PATH = 'C:/Users/Andrey/PycharmProjects/untitled/venv/Lib/site-packages/osgeo/geos_c.dll'
GDAL_LIBRARY_PATH = 'C:/Users/Andrey/PycharmProjects/untitled/venv/Lib/site-packages/osgeo/gdal300.dll'
SPATIALITE_LIBRARY_PATH = 'mod_spatialite'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'carcompany_app',
    'rest_framework',
    'reset_migrations',
    'crispy_forms',
    'django.contrib.gis',

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]

ROOT_URLCONF = 'mysite_carcompany.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'mysite_carcompany.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'
USE_TZ = True

USE_I18N = True

#USE_L10N = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
DATE_FORMAT = "Y-m-d"
USE_L10N = False
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    # глобальная настройка для стиля пагинации с указанием количества элементов на странице PAGE_SIZE
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
    # глобальная настройка для рендера json формата
}
LOGIN_REDIRECT_URL = '/api/cars/'
#LOGIN_URL = '/api/cars/'
"""
LOGIN_REDIRECT_URL = reverse_lazy('dashboard') # Сообщает о том, на какой URL-адрес перенаправлять пользователя после
# входа в систему.
LOGIN_URL = reverse_lazy('login') # URL-адрес для перенаправления пользователя на вход (с помощью декоратора l
# ogin_required)
LOGOUT_URL = reverse_lazy('logout') # URL-адрес для перенаправления пользователя на выход
"""