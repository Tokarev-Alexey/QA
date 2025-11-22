from django.db import models
import uuid

class Question(models.Model):
    text = models.TextField(verbose_name="Текст вопроса")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ['-created_at']

    def __str__(self):
        return f"Вопрос {self.id}: {self.text}"

class Answer(models.Model):
    question_id = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name="Вопрос"
    )
    user_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID пользователя"
    )
    text = models.TextField(verbose_name="Текст ответа")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ['created_at']

    def __str__(self):
        return f"Ответ {self.text} на Вопрос {self.question_id.text}"