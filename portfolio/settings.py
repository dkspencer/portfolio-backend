import os
from pathlib import Path
from django.contrib.staticfiles.storage import staticfiles_storage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

if DEBUG:
    ALLOWED_HOSTS = []

else:
    ALLOWED_HOSTS = ['daniellespencer.dev']
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'health_check',
    'health_check.db',
    'users',
    'django_filters',
    'phonenumber_field',
    'drf_spectacular',
    'rest_framework.authtoken',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
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

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASS'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': 5432,
    }

}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.CustomUser'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    'site_title': 'Portfolio',
    'site_header': 'Portfolio',
    "site_icon": staticfiles_storage.url('images/favicon.png'),
    'copyright': 'Danielle Spencer',
    'search_model': 'users.CustomUser',
    "show_ui_builder": True,
    "changeform_format": "vertical_tabs",
    "related_modal_active": True,
    'topmenu_links': [
        {
            "name": "Documentation",
            "url": "https://api.daniellespencer.dev/documentation",
            "new_window": True
        },
        {
            "name": "Dashboard",
            "url": "https://dashboard.daniellespencer.dev",
            "new_window": True
        }
    ],
    'icons': {
        'users.Customuser': 'fas fa-users',
        'users.experience': 'fas fa-briefcase',
        'users.skill': 'fas fa-laptop-code',
        'users.education': 'fas fa-graduation-cap',
        'api.question': 'fas fa-question',
        'api.answer': 'fas fa-voicemail',
        'users.project': 'fas fa-project-diagram',
        'users.link': 'fas fa-link',
        'authtoken.tokenproxy': 'fas fa-key'
    },
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'EXCEPTION_HANDLER': 'drf_pretty_exception_handler.exception_handler',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'DanielleSpencer | Portfolio',
    'DESCRIPTION': open("templates/documentation.html", "r").read(),
    'VERSION': '1.0.0',
    'CONTACT': {
        'name': 'Danielle Spencer',
        'url': 'https://daniellespencer.dev',
        'email': 'hello@daniellespencer.dev'
    },
    'EXTENSIONS_INFO': {
        'x-logo': {
            'url': staticfiles_storage.url('images/logo.png'),
            'altText': "Portfolio logo"
        }
    },
    'TAGS': [
        {
            "name": "Education",
            "description": "Users educational information."
        },
        {
            "name": "Experience",
            "description": "Users experience information."
        },
        {
            "name": "Skill",
            "description": "Users skills."
        },
        {
            "name": "User",
            "description": "User personal information including contact information."
        }
    ],
    'SERVE_INCLUDE_SCHEMA': False,
    "SWAGGER_UI_FAVICON_HREF": STATIC_URL + "images/favicon.ico"
}

HASHID_FIELD_SALT = os.environ['HASHID_FIELD_SALT']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080"
]
