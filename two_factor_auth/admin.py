from django.contrib import admin

from two_factor_auth.models import (
    Question, TwoFactorAuthenticationSession, UserAnswer, User
)

admin.site.register(User)
admin.site.register(Question)
admin.site.register(TwoFactorAuthenticationSession)
admin.site.register(UserAnswer)
admin.site.register(User)
