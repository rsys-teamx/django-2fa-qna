# django-2fa-qna


## to run

- Install twofactorauth
        pip install teamx-two-factor-auth
                    (or)
        poetry add teamx-two-factor-auth

- Add to INSTALLED_APPS
        INSTALLED_APPS = [
            ..,
            ..,
            'two_factor_auth',
            ..,
        ]

- Run migrations 

        python manage.py migrate

- Add two factor auth urls to urls.py

        url_patterns = [
            ..,
            ..,
            include('', include('two_factor_auth.urls'))
        ]

