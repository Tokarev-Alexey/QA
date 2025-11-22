from .models import Question, Answer
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'created_at']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question_id', 'user_id', 'text', 'created_at']
        read_only_fields = ['question_id']