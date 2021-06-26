from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from two_factor_auth.models import Question
from two_factor_auth.serializers import QuestionSerializer, LoginSerializer

User = get_user_model()


# class ExampleView(APIView):
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # permission_classes = [IsAuthenticated]
#
#     def post(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)


class ExampleView(GenericAPIView):
    # serializer_class = settings.SERIALIZERS.user
    # queryset = User.objects.all()

    serializer_class = LoginSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """User login with username and password."""
        # token = AuthToken.objects.create(request.user)
        authenticate(username="", password="")
        return Response({
            'user': self.get_serializer(request.user).data,
        })

    # def post(self, request, format=None):
    #     content = {
    #         'user': str(request.user),  # `django.contrib.auth.User` instance.
    #         'auth': str(request.auth),  # None
    #     }
    #     return Response(content)


class QuestionViewSet(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]
