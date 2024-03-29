import os.path
from datetime import timedelta
from pathlib import Path
from os import getenv as _


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = _('djapp_secret')

DEBUG = True

ALLOWED_HOSTS = []
BACK_HOST = 'http://localhost:8000'
FRONT_HOST = 'http://localhost:8080'

# Application definition

INSTALLED_APPS = [
    'fapp',
    'payments',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'social_django',
    'djoser',
    'django_filters',
    'celery',
    'django_celery_results',
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'fapp.middlewares.CommonTroubleshootingMiddleware'
]
CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'final_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'final_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
    #}
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'FPROJECT_DB',
        'USER': 'postgres',
        'PASSWORD': _('POSTGRES_PASSWORD'),
        'HOST': 'localhost', # change from 'localhost' to 'psql' for run with docker psql service
        'PORT': '5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Yerevan'

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = 'all_statics/'
STATIC_URL = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'
CKEDITOR_UPLOAD_PATH = 'ckmedia/'

REDIS_HOST = 'localhost' # change from 'localhost' to 'redis' for run as docker-compose service
REDIS_PORT = '6379'
CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'fapp.User'
AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'fapp.auth_backends.AuthWithEmailAndPasswordOnly',
]

SOCIAL_AUTH_PROTECTED_USER_FIELDS = ('username',)
SOCIAL_AUTH_IMMUTABLE_USER_FIELDS = ('first_name', 'last_name', )

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ('JWT', 'Bearer'),
    "ACCESS_TOKEN_LIFETIME": timedelta(seconds=30), # days=5
    "REFRESH_TOKEN_LIFETIME": timedelta(minutes=1), # days=60
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST_USER = 'vahan.grigoryan.f@gmail.com'
EMAIL_HOST_PASSWORD = _('email_access')

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    # 'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'current_user': 'fapp.serializers.UserMiniInfoSerializer'
    },
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': [
        'http://localhost:8080',
        f'{BACK_HOST}/oauth_registration',
        f'{BACK_HOST}/oauth_registration',
    ],
}
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = _('oauth2_client_id_or_key')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = _('oauth2_secret')

# LOGGING ={
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "payment_msg_with_additional_info": {
#             "format": "{levelname} {asctime} {module} {message}",
#             "style": "{",
#         }
#     },
#     "handlers": {
#         "stripe_payments_handler": {
#             "class": "logging.FileHandler",
#             "level": "DEBUG",
#             "filename": os.path.join(BASE_DIR, 'logs', 'stripe_payments.log'),
#             "formatter": "payment_msg_with_additional_info"
#         },
#     },
#     "loggers": {
#         "payments.business.payment_services.stripe_pay": {
#             "handlers": ("stripe_payments_handler", ),
#             "level": "DEBUG",
#             "propagate": False,
#         },
#     },
# }

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}
