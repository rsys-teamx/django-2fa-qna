from django.urls import path

import two_factor_auth.views as view


urlpatterns = [
    path(r'questions', view.QuestionViewSet.as_view()),
    path(r'login', view.ExampleView.as_view()),
]
