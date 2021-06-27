from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()


class HomePage(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response("Hello World")
