from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from two_factor_auth.models import Question
from two_factor_auth.serializers import QuestionSerializer


class QuestionViewSet(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]
