import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w#yh1)0w$kffiisw8@!5ju3#33&3b&vkf^qfr+j=5^u#h8zh##'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.pythonian.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'src.apps.SrcConfig',

    'ckeditor',
    'imagekit',
    'pytz',
    'crispy_forms',
    'disqus',

    'django_hosts',
]

MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',
]

ROOT_URLCONF = 'naijapodcast.urls'
ROOT_HOSTCONF = 'naijapodcast.hosts'
DEFAULT_HOST = 'www'

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

WSGI_APPLICATION = 'naijapodcast.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

SERVER_EMAIL = 'contact@naijapodcast.com'

DEFAULT_FROM_EMAIL = 'no-reply@naijapodcast.com'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'prontomaster@gmail.com'

EMAIL_HOST_PASSWORD = 'horluwasheyibellow'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_SUBJECT_PREFIX = '[Naija Podcast] '

MANAGERS = (
    ('Seyi', 'prontomaster@gmail.com'),
)

ADMINS = (
    ('Seyi', 'prontomaster@gmail.com'),
)

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap3'

DISQUS_API_KEY = 'n58mAhIU8RYgssEroy2zFJrKOmtdchvmrhTF6Bg85IGfdMMFjkc2GqdZHAsvWMtu'

DISQUS_WEBSITE_SHORTNAME = 'NaijaPodcast'