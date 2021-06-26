
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models import (
    CASCADE,
    CharField,
    IntegerField,
    DateTimeField,
    ForeignKey,
    Model,
    PositiveSmallIntegerField,
    OneToOneField,
    TextField,
    UUIDField,
    EmailField
)
from django.utils.translation import ugettext_lazy as _
from orm_choices import choices
from uuid import uuid4


@choices
class AnswerType:
    # TODO : add extension on backend to add choices
    class Meta:
        TEXT = (1, "Text")
        SELECT = (2, "Select")


class BaseModel(Model):
    id = UUIDField(default=uuid4, primary_key=True, editable=False)
    created_at = DateTimeField(auto_now_add=True, editable=False)
    updated_at = DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class User(AbstractUser, BaseModel):
    email = EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )


class TwoFactorAuthenticationSession(BaseModel):
    user = OneToOneField(get_user_model(), on_delete=CASCADE)
    questions_attempted = IntegerField(null=True)
    answer_verified = IntegerField(null=True)
    last_answer_attempt = DateTimeField(null=True)
    invalid_answer_attempts = IntegerField()

    class Meta:
        verbose_name = "2FA Session"
        verbose_name_plural = "2FA Sessions"

    def __str__(self):
        return self.id


class Question(BaseModel):
    question_desc = TextField()
    answer_type = PositiveSmallIntegerField(default=AnswerType.TEXT, choices=AnswerType.CHOICES)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question_desc


class UserAnswer(BaseModel):
    django_user = ForeignKey(get_user_model(), on_delete=CASCADE)
    question = ForeignKey(Question, on_delete=CASCADE)
    answer = TextField()

    class Meta:
        verbose_name = "User Answer"
        verbose_name_plural = "User Answers"

    def __str__(self):
        return self.id
