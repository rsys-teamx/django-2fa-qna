from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

from two_factor_auth.models import Question, UserAnswer

User = get_user_model()


class UserAuthInputSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:

                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg, code='authorization')

            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class UserQuestionSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()

    class Meta:
        model = UserAnswer
        fields = ("id", "question")

    def get_question(self, obj):
        return obj.question.question_desc


class LoginSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "questions")

    def get_questions(self, obj):
        return UserQuestionSerializer(
            obj.useranswer_set.filter(), many=True).data


class VerifyAnswerInputSerializer(serializers.Serializer):
    user_id = serializers.CharField()


class VerifyAnswerSerializer(serializers.Serializer):
    token = serializers.CharField()
