from django.contrib.auth import get_user_model, authenticate
from django.db import transaction
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from two_factor_auth.auth import add_user_answer
from two_factor_auth.models import UserAnswer
from two_factor_auth.serializers import (
    CreateUserSerializer, CreateUserAnswerSerializer
)

from two_factor_auth.models import Question, UserAnswer
from two_factor_auth.serializers import (
    QuestionSerializer, LoginSerializer, UserAuthInputSerializer,
    VerifyAnswerInputSerializer, VerifyAnswerSerializer
)

User = get_user_model()


class UserLogin(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = UserAuthInputSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response(
                {'user': self.get_serializer(user).data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class QuestionViewSet(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]


class VerifyAnswerViewSet(GenericAPIView):
    serializer_class = VerifyAnswerSerializer

    def post(self, request):
        serializer = VerifyAnswerInputSerializer(data=request.data)
        if serializer.is_valid():
            answer_count = 0
            min_answer_count = 1
            user_id = request.data.get("user_id")
            for rq in request.data.get("requests"):
                answer = UserAnswer.objects.filter(
                    django_user_id=user_id,
                    question_id=rq.get("question_id"),
                    answer__exact=rq.get("answer")
                )
                if answer.count() > 0:
                    answer_count += 1

            if answer_count >= min_answer_count:
                # Todo: Reset Session
                print(True)
                data = dict()
                data["token"] = "sdsdsd"
                return Response(
                    {'user': self.get_serializer(data).data},
                    status=status.HTTP_200_OK
                )
            else:
                # Todo: Increment Session
                print(False)
                msg = dict()
                msg["error"] = "Invalid Answers"
                return Response(msg, status=status.HTTP_401_UNAUTHORIZED)

            return Response(
                {'user': self.get_serializer(data).data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]


class UserAuthAnswerView(GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        user_id = data.get("user_id")
        requests_data = data.get("requests")
        #TODO: add auth token for this user validation

        try:
            user_obj = User.objects.get(id=user_id, is_active=True)
        except User.DoesNotExist:
            return Response("User does not exist")
        # allowed_answer = 1
        # if allowed_answer > len(auth_answer):
        #     return Response(
        #         f'Please answer question at least {allowed_answer}',
        #         status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            user_answer_serializer = CreateUserAnswerSerializer(
                data=requests_data,
                many=True,
                context={
                    'django_user': user_obj
                }
            )
            if not user_answer_serializer.is_valid():
                transaction.set_rollback(True)
                return Response(
                    user_answer_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
            user_answer_serializer.save()

        return Response("success", status=status.HTTP_200_OK)

