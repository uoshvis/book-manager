from pathlib import Path

import dj_database_url
from decouple import Csv, config
from django.contrib.messages import constants as messages


BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = config("SECRET_KEY", default="django-insecure$book_manager.settings.local")

DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost", cast=Csv())

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",

    "book_manager.apps.accounts",
    "book_manager.apps.core",
    "book_manager.apps.books",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "book_manager.urls"

INTERNAL_IPS = ["127.0.0.1"]

WSGI_APPLICATION = "book_manager.wsgi.application"

AUTH_USER_MODEL = "accounts.CustomUser"

# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL", default="postgres://book_manager:book_manager@localhost:5432/book_manager"),
        conn_max_age=600,
    )
}


# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ==============================================================================
# I18N AND L10N SETTINGS
# ==============================================================================

LANGUAGE_CODE = config("LANGUAGE_CODE", default="en-us")

TIME_ZONE = config("TIME_ZONE", default="UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [BASE_DIR / "locale"]


# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR.parent.parent / "static"

STATICFILES_DIRS = [BASE_DIR / "static"]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)


# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR.parent.parent / "media"

# ==============================================================================
# THIRD-PARTY SETTINGS
# ==============================================================================

# Django Rest Framework or Django Crispy Forms

# ==============================================================================
# FIRST-PARTY SETTINGS
# ==============================================================================

# custom settings that I may create exclusively for our project SIMPLE_XXX


BOOK_MANAGER_ENVIRONMENT = config("BOOK_MANAGER_ENVIRONMENT", default="local")

# Sets the mapping of message level to message tag, which is typically rendered as a CSS class in HTML
# Uses bootstrap contextual classes (e.g., .alert-success)

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }
