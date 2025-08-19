from django.db import models
import uuid

class ChatSession(models.Model):
    """Represents a single chat session."""
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = "Сессия чата"
        verbose_name_plural = "Сессии чата"
        ordering = ['created_at']

    def __str__(self):
        return str(self.session_id)

class ChatMessage(models.Model):
    """Represents a single message within a chat session."""
    SENDER_CHOICES = [
        ('user', 'Пользователь'),
        ('bot', 'Бот'),
    ]
    session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.CASCADE, verbose_name="Сессия")
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES, verbose_name="Отправитель")
    message = models.TextField(verbose_name="Сообщение")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Время отправки")

    class Meta:
        verbose_name = "Сообщение чата"
        verbose_name_plural = "Сообщения чата"
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.get_sender_display()}: {self.message[:50]}"