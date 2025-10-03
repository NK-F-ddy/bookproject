"""
Django settings for bookproject project.
"""

import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ----------------------------------------------------
# 💡 重要な修正点 1: SECRET_KEYとDEBUGを本番環境対応に
# ----------------------------------------------------

# 環境変数からSECRET_KEYを読み込む。ローカルでの開発用にダミーを設定。
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-4^7m-5h)^$n4qdeh*8ta*pyvb7mz=_ma6i3*5c74i^ejo-$lu2')

# Render環境ではDEBUG=False、ローカルではTrueとする。
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

# 本番環境ではRenderのホスト名を含むすべてのホストを許可（環境変数依存）
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')
if DEBUG:
    ALLOWED_HOSTS = ['*'] # ローカル環境では全て許可


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'book.apps.BookConfig',
]

# ----------------------------------------------------
# 💡 重要な修正点 2: MIDDLEWAREのカンマとWhiteNoiseの配置
# ----------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # 💡 ここに配置（カンマ忘れも修正）
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'bookproject.wsgi.application'


# Database
# ----------------------------------------------------
# 💡 重要な修正点 3: データベース設定を環境変数から読み込む
# ----------------------------------------------------

# 開発時はSQLite、本番環境ではPostgreSQL接続情報（DATABASE_URL）を使用
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        conn_max_age=600
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# ----------------------------------------------------
# 💡 重要な修正点 4: STATIC_ROOTの追加
# ----------------------------------------------------

STATIC_ROOT = BASE_DIR / 'staticfiles' # 💡 collectstaticの出力先

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'
