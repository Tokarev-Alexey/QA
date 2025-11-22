from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from .services import AnswerService


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer
    pagination_class = PageNumberPagination
    http_method_names = ['get','post', 'delete']

    @action(detail=True, methods=['post'])
    def answers(self, request: Request, pk: int | None = None) -> Response:
        question = self.get_object()
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            answer = AnswerService.create_answer(question, serializer.validated_data)
            return Response(AnswerSerializer(answer).data, status=201)
        return Response(serializer.errors, status=400)

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('-created_at')
    serializer_class = AnswerSerializer
    http_method_names = ['get', 'delete']  # Только GET и DELETE
