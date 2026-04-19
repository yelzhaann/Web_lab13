# settings.py ішіне қосу керек бөліктер:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',          # ← өз қосымшаңызды тіркеу
]

# Шаблондар орналасқан жерді Django таба алу үшін:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'accounts' / 'templates'],  # ← base.html осында
        'APP_DIRS': True,   # accounts/templates/accounts/ папкасын автоматты табады
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',   # ← user объектісі
                'django.contrib.messages.context_processors.messages',  # ← messages
            ],
        },
    },
]

# Пайдаланушы кіргеннен кейін қайда жіберіледі (әдепкі)
LOGIN_REDIRECT_URL = 'dashboard'

# @login_required декораторы авторизациясыз қолданушыны қай бетке жіберу керек
LOGIN_URL = 'login'
