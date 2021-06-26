from datetime import timezone
from datetime import datetime, timedelta

from django.db.models import F
from rest_framework.exceptions import ValidationError

from two_factor_auth.models import TwoFactorAuthenticationSession


def update_2fa_session(user_id, invalid_attempt=False):
    if invalid_attempt:
        TwoFactorAuthenticationSession.objects.filter(user_id=user_id).update(
            last_answer_attempt=datetime.now(),
            invalid_answer_attempts=F("invalid_answer_attempts") + 1
        )


def check_2fa_login_attempt(user_id):
    msg = dict()
    try:
        session, created = TwoFactorAuthenticationSession.objects.get_or_create(
            user_id=user_id, defaults={
                "last_answer_attempt": datetime.now(),
                "invalid_answer_attempts": 0
            }
        )
        retry_in_minutes = 1
        invalid_attempt_limit = 2
        if session.invalid_answer_attempts >= invalid_attempt_limit:
            if datetime.now(timezone.utc) - session.last_answer_attempt < timedelta(
                minutes=retry_in_minutes
            ):
                rem = (
                        session.last_answer_attempt + timedelta(minutes=retry_in_minutes) -
                        datetime.now(timezone.utc) + timedelta(minutes=0)
                )
                msg["error"] = f"Invalid Attempts Exceeded, Try After {rem}"
                raise ValidationError(msg, code="authorization")
            else:
                TwoFactorAuthenticationSession.objects.filter(user_id=user_id).delete()

    except TwoFactorAuthenticationSession.DoesNotExist:
        msg = dict()
        msg["error"] = "Invalid User"
        raise ValidationError(msg, code="authorization")
