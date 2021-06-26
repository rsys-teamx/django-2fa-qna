from django.contrib.auth import get_user_model, authenticate
from rest_framework.serializers import (
    Serializer, CharField, ValidationError, SerializerMethodField, UUIDField)

User = get_user_model()
from hashlib import md5
from rest_framework.serializers import ModelSerializer
from two_factor_auth.models import Question, UserAnswer
from two_factor_auth.models import User


class UserAuthInputSerializer(Serializer):
    username = CharField()
    password = CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:

                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise ValidationError(msg, code='authorization')

            else:
                msg = 'Unable to log in with provided credentials.'
                raise ValidationError(msg, code='authorization')

        else:
            msg = 'Must include "username" and "password".'
            raise ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class UserQuestionSerializer(ModelSerializer):
    question = SerializerMethodField()

    class Meta:
        model = UserAnswer
        fields = ("id", "question")

    def get_question(self, obj):
        return obj.question.question_desc


class LoginSerializer(ModelSerializer):
    questions = SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "questions")

    def get_questions(self, obj):
        return UserQuestionSerializer(
            obj.useranswer_set.filter(), many=True).data


class VerifyAnswerInputSerializer(Serializer):
    user_id = CharField()


class VerifyAnswerSerializer(Serializer):
    refresh = CharField()
    access = CharField()


class QuestionSerializer(ModelSerializer):
    question = SerializerMethodField()

    class Meta:
        model = UserAnswer
        fields = ("id", "question")

    def get_question(self, obj):
        return obj.question.question_desc


class CreateUserAnswerSerializer(ModelSerializer):
    question_id = UUIDField(required=True)

    class Meta:
        model = UserAnswer
        fields = ('question_id', 'answer')

    def create(self, validated_data):
        django_user = self.context.get('django_user')
        validated_data['django_user'] = django_user
        validated_data['answer'] = md5(validated_data['answer'].encode()).hexdigest()
        return UserAnswer.objects.create(**validated_data)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'password'
        )

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        return User.objects.create(**validated_data)
