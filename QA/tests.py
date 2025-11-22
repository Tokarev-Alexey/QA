import pytest
from .models import Question, Answer


#тест на создание вопроса
@pytest.mark.django_db
def test_question_creation():
    question = Question.objects.create(text="Test question?")
    assert question.text == "Test question?"
    assert question.created_at is not None

#тест на создание отве
@pytest.mark.django_db
def test_answer_creation():
    question = Question.objects.create(text="Test question?")
    answer = Answer.objects.create(question_id=question, text="Test answer")
    assert answer.question_id == question
    assert answer.text == "Test answer"