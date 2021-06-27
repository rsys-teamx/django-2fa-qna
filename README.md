# django-2fa-qna

 Python Package - [Teamx Two Factor Authentication](https://pypi.org/project/teamx-two-factor-auth/)


## to run

- Install twofactorauth

        pip install teamx-two-factor-auth
                    (or)
        poetry add teamx-two-factor-auth

- Add to INSTALLED_APPS in settings.py

        INSTALLED_APPS = [
            ..,
            ..,
            'two_factor_auth',
            'rest_framework',
            'rest_framework.authtoken',
            ..,
        ]

- update or extend AUTH_USER_MODEL and othre config values in settings.py

        AUTH_USER_MODEL = "two_factor_auth.User"  # can be overridden
        REGISTRATION_QUESTIONS_COUNT = 3  # questions users have to select while register
        USER_REGISTRATION_MIN_ANSWER_COUNT = 2  # minimum answers they user has to get right to login
        INVALID_ATTEMPTS_LIMIT = 2  # max number of invalid attempts before user is locked
        ANSWER_ATTEMPTS_RETRY_LIFETIME = datetime.timedelta(minutes=1)  # cooldown time for retrying answers
        USER_QUESTION_CHANGE_FREQUENCY = datetime.timedelta(days=60)  # time when user has to change their questions
        MAX_ANSWER_CHARACTER_LENGTH = 12  # maximum length for answers

- Run migrations 

        python manage.py migrate

- Add two factor auth urls to urls.py 

        url_patterns = [
            ..,
            ..,
            path('2fa/', include('two_factor_auth.urls'))
        ]


- Run server

