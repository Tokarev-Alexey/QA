from .models import Question, Answer


class AnswerService:
    @staticmethod
    def create_answer(question: Question, validated_data: dict) -> Answer:
        return Answer.objects.create(question_id=question, **validated_data)
