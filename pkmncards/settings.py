from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================================
# Core
# ==========================================================

SECRET_KEY = "change-me"

DEBUG = True

ALLOWED_HOSTS = []

# ==========================================================
# Applications
# ==========================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # tes apps
    "cards",
]

# ==========================================================
# Middleware
# ==========================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pkmncards.urls"

# ==========================================================
# Templates
# ==========================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pkmncards.wsgi.application"

# ==========================================================
# Database
# ==========================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ==========================================================
# Internationalisation
# ==========================================================

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True
USE_TZ = True

# ==========================================================
# Static files
# ==========================================================

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# uniquement utile plus tard en prod
STATIC_ROOT = BASE_DIR / "staticfiles"

# ==========================================================
# Default primary key
# ==========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
