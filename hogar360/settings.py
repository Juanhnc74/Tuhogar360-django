from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(wq^r3+hjx+#*)&wj7o2hpznwf81spwz^1#x$+p)4dszbr=a!b'

# SECURITY WARNING: don't run with debug turned on in production!

RAILWAY_DOMAIN = os.getenv("RAILWAY_URL", "https://tuhogar360.up.railway.app")

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '127.0.0.1:8000', 'https://tuhogar360.up.railway.app/', 'tuhogar360.up.railway.app', 'RAILWAY_DOMAIN']



DEBUG = False
# Agrega el dominio de Railway a la lista de orígenes confiables para CSRF
CSRF_TRUSTED_ORIGINS = [RAILWAY_DOMAIN]

# Application definition



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'administrativos',
    'usuarios',
    'catalogo',
    'blog',
    'subscriptions',
    'crispy_forms',
    'crispy_bootstrap4',
    'djstripe',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'hogar360.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'hogar360.wsgi.application'


# Database
''''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
#'ENGINE': 'django.db.backends.sqlite3',
#      'NAME': BASE_DIR / 'db.sqlite3',
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'MuNmSxGItlhIPBtltaHTgspECtboHWtj',
        'HOST': 'viaduct.proxy.rlwy.net',
        'PORT': '56397',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGES = [
    ('es', 'Spanish'),
    ('es-mx', 'Spanish (Mexico)'),
]

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'usuarios/static'),
    os.path.join(BASE_DIR, 'administrativos/static'),
    os.path.join(BASE_DIR, 'catalogo/static'),
    os.path.join(BASE_DIR, 'blog/static'),
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings.py
AUTH_USER_MODEL = 'usuarios.CustomUser'


CRISPY_ALLOED_TEMPLATED_PACK = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"


LOGIN_URL = '/ingreso/'


#Manejo de imagenes
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#Stripe settings email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#Stripe settings
STRIPE_TEST_PUBLIC_KEY = os.environ.get("STRIPE_TEST_PUBLIC_KEY", "pk_test_51ODKwZEVbfr5OPjDTHqJu0rMsA8ZiWpbnf5cWvjBsX8IrTqViXbGUFr3pyqFZDkuGpIBvFyUMAvE955bxdyYDfgx00ZM62NB0V")
STRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "sk_test_51ODKwZEVbfr5OPjD1nyyolXyJfGoZjBJXUNJSA9dcDtaLWCiMnQff2TakKP8lWTKR1Vg0Dbgd3sbj6cAiv1YkcfV00bQ3rxBct")
STRIPE_LIVE_MODE = False
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"
DJSTRIPE_WEBHOOK_SECRET = os.environ.get("DJSTRIPE_WEBHOOK_SECRET", "whsec_09501c4a4ec76443530a09aaf35f5a72858b9c733a8b75ab568ea0ca57bc3ccb")
STRIPE_PRICING_TABLE_ID = "prctbl_1PDaVBEVbfr5OPjDHJcLHtOK"

