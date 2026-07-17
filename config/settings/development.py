from .base import *

from decouple import config
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": dj_database_url.config(
        default=config("DEV_DATABASE_URL")
    )
}