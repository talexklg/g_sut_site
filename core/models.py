from django.db import models

class Achievement(models.Model):
    """Model for an achievement."""
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    date = models.DateField(verbose_name="Дата")
    image = models.ImageField(upload_to='achievements/', blank=True, null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"
        ordering = ['date']

    def __str__(self):
        return self.title