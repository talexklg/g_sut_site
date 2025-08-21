from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class NewsArticle(models.Model):
    """Model for a news article."""
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Автор")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name="Изображение (файл)")
    image_url = models.URLField(blank=True, null=True, verbose_name="Изображение (ссылка)")
    video = models.FileField(upload_to='news_videos/', blank=True, null=True, verbose_name="Видео (файл)")
    video_url = models.URLField(blank=True, null=True, verbose_name="Видео (ссылка)")

    def clean(self):
        if self.image and self.image_url:
            raise ValidationError("Пожалуйста, укажите что-то одно: или файл изображения, или ссылку на него.")
        if self.video and self.video_url:
            raise ValidationError("Пожалуйста, укажите что-то одно: или файл видео, или ссылку на него.")

    @property
    def get_image_url(self):
        if self.image_url:
            return self.image_url
        if self.image:
            return self.image.url
        return None

    @property
    def get_video_url(self):
        if self.video_url:
            return self.video_url
        if self.video:
            return self.video.url
        return None

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

    image = models.ImageField(upload_to='contest_images/', blank=True, null=True, verbose_name="Изображение (файл)")
    image_url = models.URLField(blank=True, null=True, verbose_name="Изображение (ссылка)")
    video = models.FileField(upload_to='contest_videos/', blank=True, null=True, verbose_name="Видео (файл)")
    video_url = models.URLField(blank=True, null=True, verbose_name="Видео (ссылка)")

    def clean(self):
        if self.image and self.image_url:
            raise ValidationError("Пожалуйста, укажите что-то одно: или файл изображения, или ссылку на него.")
        if self.video and self.video_url:
            raise ValidationError("Пожалуйста, укажите что-то одно: или файл видео, или ссылку на него.")

    @property
    def get_image_url(self):
        if self.image_url:
            return self.image_url
        if self.image:
            return self.image.url
        return None

    @property
    def get_video_url(self):
        if self.video_url:
            return self.video_url
        if self.video:
            return self.video.url
        return None

    class Meta:
        verbose_name = "Конкурс"
        verbose_name_plural = "Конкурсы"
        ordering = ['start_date']

    def __str__(self):
        return self.title
