
from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
    PositiveSmallIntegerField,
    TextField,
    UUIDField,
)
from orm_choices import choices
from uuid import uuid4


@choices
class AnswerType:
    # TODO : add extension on backend to add choices
    class Meta:
        TEXT = (1, "Text")
        SELECT = (2, "Select")


class User(AbstractUser):
    id = UUIDField(default=uuid4, primary_key=True, editable=False)
    created_at = DateTimeField(auto_now_add=True, editable=False)
    updated_at = DateTimeField(auto_now=True, editable=False)


class Questions(Model):
    id = UUIDField(default=uuid4, primary_key=True, editable=False)
    question_desc = TextField()
    answer_type = PositiveSmallIntegerField(default=AnswerType.TEXT, choices=AnswerType.CHOICES)
    created_at = DateTimeField(auto_now_add=True, editable=False)
    updated_at = DateTimeField(auto_now=True, editable=False)


class UserAnswer(Model):
    id = UUIDField(default=uuid4, primary_key=True, editable=False)
    django_user = ForeignKey(User, on_delete=CASCADE)
    question = ForeignKey(Questions, on_delete=CASCADE)
    answer = TextField()
    created_at = DateTimeField(auto_now_add=True, editable=False)
    updated_at = DateTimeField(auto_now=True, editable=False)
