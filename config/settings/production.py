from .base import *

from decouple import config
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = [
    ".onrender.com",
]

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL")
    )
}

CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]

TWELVE_DATA_API_KEY = config("TWELVE_DATA_API_KEY")