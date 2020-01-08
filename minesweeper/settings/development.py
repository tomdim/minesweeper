from .base import *

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('MS_DATABASE_NAME', 'minesweeper'),
        'USER': os.environ.get('MS_DATABASE_USER', 'postgres'),
        'PASSWORD': os.environ.get('MS_DATABASE_PASS', '1234'),
        'HOST': os.environ.get('MS_DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('MS_DATABASE_PORT', '5432'),
    },
}
