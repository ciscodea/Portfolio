from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Secure redirect https
SECURE_SSL_REDIRECT = True

# Database
import dj_database_url
from decouple import config
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

#For deployment purposes
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Clodinary for storage images
import cloudinary
import cloudinary.uploader
import cloudinary.api

#For deployment purposes
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'he9xujseo',
    'API_KEY': '254211853684524',
    'API_SECRET': 'SrF6WiXygiXs3UpkHH-hk8iIFAc',
}
