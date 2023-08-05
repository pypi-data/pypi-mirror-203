from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure--t@#-_5%%8%=6rg=byg75+d0z8rn&2jj!ce*12fpr*%2kbcabj'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kfsdutils.apps.endpoints',
]

MIDDLEWARE = [
    'kfsdutils.apps.middleware.configuration.KubefacetsConfigMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'kfsdutils.apps.middleware.auth.KubefacetsAuthMiddleware',
]

ROOT_URLCONF = 'kfsdutils.urls'

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

WSGI_APPLICATION = 'kfsdutils.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'TEST_REQUEST_RENDERER_CLASSES': (
        'kfsdutils.apps.endpoints.renderers.kubefacetsjson.KubefacetsJSONRenderer',
        'kfsdutils.apps.endpoints.renderers.kubefacetsyaml.KubefacetsYAMLRenderer',
    ),
    'KUBEFACETS': {
        "STACKTRACE": False
    },
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'EXCEPTION_HANDLER': 'kfsdutils.apps.endpoints.exceptions.KubefacetsAPIExceptionHandler',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'kfsdutils.apps.endpoints.middleware.be_auth.ApiKeyAuthentication'
    ],
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 300,
    }
}

KUBEFACETS = {
    "config": {
        "is_local_config": True,
        "lookup_dimension_keys": ["env"],
        "local": [
            {
                "setting": ["master"],
                "certs": {
                    "host": "http://localhost:8002",
                    "jwt_authority_id": "ORG=Kubefacets,APP=Certs,PRJ=Auth,COLL=Login,JWT=Login",
                    "token_gen_uri": "jwt-authorities/{}/token/gen/",
                    "token_publickey_uri": "jwt-authorities/{}/publickey/",
                    "token_decode_uri": "jwt-authorities/{}/token/dec/",
                    "tokens": {
                        "access": {
                            "lifetime_in_mins": 30
                        },
                        "refresh": {
                            "lifetime_in_mins": 300
                        }
                    }
                },
                "auth_fe": {
                    "host": "http://localhost:8000",
                    "login_url": "accounts/signin/",
                    "verify_email_url": "accounts/register/email/",
                    "register_verify_success_url": "http://localhost:8000/accounts/index"
                },
                "auth_api": {
                    "host": "http://localhost:8001",
                    "api_key": "9a02f7923aa22e69e0e2858d682a0c227ae0f3ce125a41c61d",
                    "user_login_url": "login/user/",
                    "user_register_url": "user/",
                    "user_exists_url": "user/{}/",
                    "verify_email_url": "verify/",
                    "verify_tmp_tokens_url": "verify/{}/tokens/",
                    "user_tokens_url": "tokens/{}/login/",
                    "token_extract_url": "tokens/extract/",
                    "access_token_refresh_url": "tokens/access/renew/",
                    "user_identifier_prefix": "USER={}"
                },
                "cookie": {
                    "access": {
                        "key": "access_token",
                        "secure": False,
                        "http_only": True,
                        "same_site": "lax"
                    },
                    "refresh": {
                        "key": "refresh_token",
                        "secure": False,
                        "http_only": True,
                        "same_site": "lax"
                    }
                }
            },
            {
                "setting": ["env:dev"],
                "certs": {
                    "host": "http://localhost:8002/"
                }
            }
        ]
    }
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Auth as a Service',
    'VERSION': '1.0.0',
    "COMPONENT_SPLIT_REQUEST": True,
    "ENUM_ADD_EXPLICIT_BLANK_NULL_CHOICE": False,
    'SERVE_INCLUDE_SCHEMA': False,
    "POSTPROCESSING_HOOKS": [
        "drf_spectacular.hooks.postprocess_schema_enums",
    ],
    'SERVE_AUTHENTICATION': None,
    "APPEND_COMPONENTS": {
        "securitySchemes": {
            "ApiKeyAuth": {
                "type": "apiKey",
                "in": "header",
                "name": "X-APIKey"
            }
        }
    },
    "SECURITY": [{"ApiKeyAuth": [], }],
}
