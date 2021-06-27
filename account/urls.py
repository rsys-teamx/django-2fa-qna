from django.urls import path
from rest_framework.authtoken import views

import account.views as view


urlpatterns = [
    path(r"home/", view.HomePage.as_view(), name="home"),
    path("api-token-auth/", views.obtain_auth_token, name="api-tokn-auth"),
]
