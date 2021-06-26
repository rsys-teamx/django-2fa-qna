
from hashlib import md5
from two_factor_auth.models import Questions, UserAnswer


def AddQuestion(f):
    def wrapper(*args, **kwargs):
        add_question(**kwargs)
    return wrapper


def AddUserAnswer(f):
    def wrapper(*args, **kwargs):
        add_user_answer(**kwargs)
    return wrapper


def CheckAnswer(f):
    def wrapper(*args, **kwargs):
        validated = validate_answer(
            kwargs["user_id"],
            kwargs["question_id"],
            kwargs["answer"]
        )
        return f(*args, **kwargs) if validated else None
    return wrapper


def add_question(**values):
    Questions.objects.create(**values)


def add_user_answer(**values):
    values["answer"] = md5(values["answer"].encode()).hexdigest()
    UserAnswer.objects.create(**values)


def valdate_answer(user_id, question_id, answer):
    try:
        user_answer = UserAnswer.objects.get(user_id=user_id, question_id=question_id)
        if user_anser.answer == md5(answer.encode()).hexdigest():
            return True
        else:
            return False
    except UserAnswer.DoesNotExist:
        return False
