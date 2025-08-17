from django.db import models

class Album(models.Model):
    """Model for a photo album."""
    title = models.CharField(max_length=255, verbose_name="Название альбома")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ['created_at']

    def __str__(self):
        return self.title

class Photo(models.Model):
    """Model for a photo."""
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos', verbose_name="Альбом")
    title = models.CharField(max_length=255, blank=True, verbose_name="Название фото")
    image = models.ImageField(upload_to='gallery/', verbose_name="Изображение")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
        ordering = ['uploaded_at']

    def __str__(self):
        return self.title or f"Фото {self.id}"

class Video(models.Model):
    """Model for a video."""
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='videos', verbose_name="Альбом")
    title = models.CharField(max_length=255, blank=True, verbose_name="Название видео")
    video_file = models.FileField(upload_to='gallery/videos/', verbose_name="Видеофайл")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
        ordering = ['uploaded_at']

    def __str__(self):
        return self.title or f"Видео {self.id}"