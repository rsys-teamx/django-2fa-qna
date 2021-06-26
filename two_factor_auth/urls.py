from django.urls import path
from rest_framework.authtoken import views

import two_factor_auth.views as view


urlpatterns = [
    path(r'home', view.HomePage.as_view()),
    path(r'questions', view.QuestionViewSet.as_view()),
    path(r'login', view.UserLogin.as_view()),
    path(r'2fa-verify-answer', view.VerifyAnswerViewSet.as_view()),
    path(r'register', view.UserRegistrationViewSet.as_view()),
    path(r'auth-questions', view.UserAuthAnswerView.as_view()),
    path('api-token-auth', views.obtain_auth_token, name='api-tokn-auth'),
]
