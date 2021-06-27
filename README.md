# django-2fa-qna


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
            ..,
        ]

- update or extend AUTH_USER_MODEL and othre config values in settings.py

        AUTH_USER_MODEL = 'two_factor_auth.User'  # optional can be overridden
        MIN_QUESTIONS = 3  
        MIN_ANSWERS = 2  
        QUESTION_CHANGE_FREQUENCY = 90  # days
        ANSWER_ATTEMPTS = 1  # 3 tries
        MAX_ANSWER_LENGTH = 12  # characters

- Run migrations 

        python manage.py migrate

- Add two factor auth urls to urls.py

        url_patterns = [
            ..,
            ..,
            include('', include('two_factor_auth.urls'))
        ]

