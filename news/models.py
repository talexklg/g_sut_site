from django.db import models
from django.contrib.auth.models import User

class NewsArticle(models.Model):
    """Model for a news article."""
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Автор")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['pub_date']

    def __str__(self):
        return self.title

class Contest(models.Model):
    """Model for a contest."""
    title = models.CharField(max_length=255, verbose_name="Название конкурса")
    description = models.TextField(verbose_name="Описание")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(blank=True, null=True, verbose_name="Дата окончания")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Конкурс"
        verbose_name_plural = "Конкурсы"
        ordering = ['start_date']

    def __str__(self):
        return self.title
