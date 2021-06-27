from django.contrib.auth.models import AbstractUser
from django.db.models import DateTimeField, Model, UUIDField, EmailField
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4


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
