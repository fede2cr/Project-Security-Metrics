"""
Global Settings

Per-environment settings are read from a .env file.
"""
import os
import sys

from dotenv import load_dotenv

load_dotenv(verbose=True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG")

INTERNAL_IPS = [
    "127.0.0.1",
]

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "taggit",
    "rest_framework",
    "oss",
]
if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "core.wsgi.application"

# Database Information
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": u"[%(asctime)s] %(levelname)s [%(module)s.%(funcName)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "simple": {"format": u"%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "verbose",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.getenv("LOG_FILENAME"),
            "formatter": "verbose",
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "root": {"handlers": ["console", "file"], "level": "INFO"},
        "oss": {"handlers": ["file", "console"], "level": "DEBUG", "propagate": True},
        "urllib3": {"handlers": ["console"], "level": "DEBUG"},
    },
}

if os.getenv("CACHE_ENABLED"):
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
            "LOCATION": os.getenv("CACHE_FILENAME"),
        }
    }

# Tokens for accessing the GitHub API
GITHUB_TOKENS = os.getenv("GITHUB_TOKENS")

# FastSquat Typo-Squatting Service
FASTSQUAT_API_ENDPOINT = os.getenv("FASTSQUAT_API_ENDPOINT")
FASTSQUAT_API_TOKEN = os.getenv("FASTSQUAT_API_TOKEN")

# Work Queue
DEFAULT_QUEUE_CONNECTION_STRING = os.getenv("DEFAULT_QUEUE_CONNECTION_STRING")
DEFAULT_QUEUE_WORK_TO_DO = os.getenv("DEFAULT_QUEUE_WORK_TO_DO")
DEFAULT_QUEUE_WORK_COMPLETE = os.getenv("DEFAULT_QUEUE_WORK_COMPLETE")
DEFAULT_QUEUE_WORK_IMPORT = os.getenv("DEFAULT_QUEUE_WORK_IMPORT")
