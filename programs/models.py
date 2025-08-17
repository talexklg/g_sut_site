from django.db import models

class Teacher(models.Model):
    """Model for a teacher."""
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True, verbose_name="Фото")
    bio = models.TextField(blank=True, verbose_name="Биография")
    experience = models.CharField(max_length=100, blank=True, verbose_name="Опыт работы")
    phone_work = models.CharField(max_length=20, blank=True, null=True, verbose_name="Рабочий телефон")
    phone_mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name="Мобильный телефон")
    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name="Электронная почта")
    telegram_messenger = models.CharField(max_length=100, blank=True, null=True, verbose_name="Telegram")
    max_messenger = models.CharField(max_length=100, blank=True, null=True, verbose_name="MAX-мессенджер")
    other_contacts = models.TextField(blank=True, null=True, verbose_name="Другие контакты")

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return self.full_name

class Program(models.Model):
    """Model for a program."""
    name = models.CharField(max_length=255, verbose_name="Название программы")
    description = models.TextField(verbose_name="Описание")
    age_group = models.CharField(max_length=50, verbose_name="Возрастная группа")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='programs', verbose_name="Преподаватель")
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"

    def __str__(self):
        return self.name