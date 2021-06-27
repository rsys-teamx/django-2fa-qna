# django-2fa-qna

 Python Package - [Django Two Factor Auth QnA](https://pypi.org/project/django-two-factor-auth-qna/)

We are using Both Django DRF - TokenAuthentication and djangorestframework-simplejwt.
2FA will be using JWT Tokens to Authenticate. TokenAuthentication is used in Register and Login endpoints to generate token for temporary user authentication.


## to run

- Install twofactorauth

        pip install django-two-factor-auth-qna
                    (or)
        poetry add django-two-factor-auth-qna

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


- To add questions 
 
         ./manage.py createsuperuser   # enter creadentials
         ./manage.py runserver  
         #  open server_address:port/admin  , login and add/import questions


- Run server

Using Black for Python Lint Validation

