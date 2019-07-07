import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'dxuv@y=y4+kxacm%0a-hs3v8$#+kx7(98r@(*cy7-l11n6!zw&'
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', # add this
    'corsheaders', # add this
    'app', # add this
    'django_slack' 
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # add this
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# add this block below MIDDLEWARE
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)

ROOT_URLCONF = 'api.urls'

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

WSGI_APPLICATION = 'api.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'homepagedb',
        'USER': 'neekey',
        'PASSWORD': '#nky%2T0A1K9A0D6A0T1',
        'HOST': '',
        'POST': '',
    }
}


# Password validation
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
LANGUAGE_CODE = 'ja'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

DEBUG = False # True => Falseにする

ALLOWED_HOSTS = ["ec2-3-112-249-151.ap-northeast-1.compute.amazonaws.com"] # Hostを追記
#(省略)
STATIC_URL = '/static/' # 基本これで決め打ち
STATIC_ROOT = os.path.join(BASE_DIR, 'static')



# add the following just below STATIC_URL
MEDIA_URL = '/media/' # add this
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # add this

# SLACK_WEBHOOK_ENDPOINT = 'https://hooks.slack.com/services/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'
SLACK_TOKEN = 'https://hooks.slack.com/services/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'
SLACK_CHANNEL = '#neekey'
SLACK_USERNAME = u'me'
SLACK_ICON_EMOJI = u':ghost:'
SLACK_FAIL_SILENTLY = True