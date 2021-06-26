from django.contrib.auth import get_user_model
from rest_framework import serializers

from two_factor_auth.models import Question, UserAnswer

User = get_user_model()


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class UserQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all'


class LoginSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', "questions")

    def get_questions(self, obj):
        return UserQuestionSerializer(
            obj.useranswer_set.filter(), many=True).data
