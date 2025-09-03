from .base import *
from decouple import config, Csv, RepositoryEnv, Config
from pathlib import Path
from mongoengine import connect

env_path = Path(__file__).resolve().parent.parent / ".env.local"
config = Config(RepositoryEnv(env_path))

# Security
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['127.0.0.1','localhost']

# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT'),
    }
}

# MongoDB
connect(
    db=config('MONGO_DB'),
    host=config('MONGO_HOST'),
    port=config('MONGO_PORT', cast=int),
    username=config('MONGO_USER'),
    password=config('MONGO_PASSWORD'),
    authentication_source=config('MONGO_DB')
)

# Neo4j
# NEOMODEL_NEO4J_BOLT_URL = f"bolt://{config('NEO4J_USER')}:{config('NEO4J_PASSWORD')}@{config('NEO4J_HOST')}:{config('NEO4J_PORT')}"
# NEOMODEL_SIGNALS = True
# NEOMODEL_FORCE_TIMEZONE = True
