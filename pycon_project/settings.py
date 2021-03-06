# -*- coding: utf-8 -*-
# Django settings for layer zero pinax project.

import os.path
import posixpath
import pinax

PINAX_ROOT = os.path.abspath(os.path.dirname(pinax.__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

PYCON_YEAR = "2012"

# tells Pinax to use the default theme
PINAX_THEME = "default"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
]

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "data.db", # Or path to database file if using sqlite3.
        "USER": "",                             # Not used with sqlite3.
        "PASSWORD": "",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Asia/Taipei"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "zh-TW"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/%s/site_media/media/" % PYCON_YEAR

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/%s/site_media/static/" % PYCON_YEAR

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static", PYCON_YEAR),
    os.path.join(PINAX_ROOT, "themes", PINAX_THEME, "static"),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Make this unique, and don't share it with anybody.
SECRET_KEY = ""

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.load_template_source",
    "django.template.loaders.app_directories.load_template_source",
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_openid.consumer.SessionConsumer",
    "django.contrib.messages.middleware.MessageMiddleware",
    "pinax.middleware.security.HideSensistiveFieldsMiddleware",
    "reversion.middleware.RevisionMiddleware",
    #"debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "pycon_project.urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "pinax.core.context_processors.pinax_settings",
    "pinax.apps.account.context_processors.account",
    "symposion.review.context_processors.permissions",
]

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.humanize",
    "django.contrib.staticfiles",
    "bootstrapform",
    "gunicorn",
    "nashvegas",
    "django_extensions",
    "common",
    
    # external
    "uni_form",
    "debug_toolbar",
    "markitup",
    
    "emailconfirmation",
    "timezones",
    "django_openid",
    "oauth_access",
    "uni_form",
    "ajax_validation",
    "fixture_generator",
    "wakawaka",
    "biblion",
    "fixture_generator",
    "sorl.thumbnail",
    "mailout",
    "reversion",
    
    # Pinax
    "pinax.templatetags",
    "pinax.apps.waitinglist",
    "pinax.apps.account",
    "pinax.apps.analytics",
    
    # symposion
    "symposion.conference",
    "symposion.proposals",
    "symposion.review",
    "symposion.schedule",
    "symposion.speakers",
    "symposion.sponsors_pro",
    
    # project
    "boxes",
    "wiki",
]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

CONTACT_EMAIL = "organizers@pycon.tw"
SITE_NAME = "PyCon Taiwan 2012"

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

BIBLION_PARSER = ["wiki.markdown_parser.parse", {}]
BIBLION_SECTIONS = [
    ("general", "General"),
    ("announcement", "Announcement"),
]

ACCOUNT_OPEN_SIGNUP = False
ACCOUNT_REQUIRED_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = True
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = True

AUTHENTICATION_BACKENDS = [
    "pinax.apps.account.auth_backends.AuthenticationBackend",
]

LOGIN_REDIRECT_URLNAME = "home"
LOGIN_URL = "/%s/account/login/" % PYCON_YEAR
LOGOUT_URL = "/%s/account/logout/" % PYCON_YEAR
LOGIN_REDIRECT_URLNAME = "home"

EMAIL_CONFIRMATION_DAYS = 3

WAKAWAKA_DEFAULT_INDEX = "index"
WAKAWAKA_SLUG_REGEX = r"((\w{2,})(/\w{2,})*)" # allow lower case wiki page names
WAKAWAKA_LOCK_TIMEOUT = 10*60

MARKITUP_AUTO_PREVIEW = True
MARKITUP_SET = "markitup/sets/markdown-custom"
MARKITUP_SKIN = "markitup/skins/simple"
MARKITUP_FILTER = ("wiki.markdown_parser.parse", {})
MARKITUP_MEDIA_URL = STATIC_URL

ACCEPTING_PROPOSALS = True

SCHEDULE_TIMEZONE = "Asia/Taipei"

MAILOUT_MODULES = [
    "symposion.email_lists.organizers",
]

REDIS_PARAMS = dict(host="127.0.0.1")

ANALYTICS_SETTINGS = {
    "google": {
        "2": "UA-2401894-29", # staging
        "3": "UA-2401894-29", # production
    }
}

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass

DEFAULT_FROM_EMAIL = "mailer@pycon.tw"

LANGUAGES = (
    ('en', 'English'),
    ('zh-tw', 'Traditional Chinese'),
)

LOCALE_PATHS = os.path.join(PROJECT_ROOT, 'locale')
