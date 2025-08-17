from django.db import models
from programs.models import Program, Teacher

class ScheduleEntry(models.Model):
    """Model for a schedule entry."""
    DAY_CHOICES = [
        ('MON', 'Понедельник'),
        ('TUE', 'Вторник'),
        ('WED', 'Среда'),
        ('THU', 'Четверг'),
        ('FRI', 'Пятница'),
        ('SAT', 'Суббота'),
        ('SUN', 'Воскресенье'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название занятия")
    description = models.TextField(blank=True, verbose_name="Описание")
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Программа")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Преподаватель")
    day_of_week = models.CharField(max_length=3, choices=DAY_CHOICES, verbose_name="День недели")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    room = models.CharField(max_length=100, blank=True, verbose_name="Кабинет")

    class Meta:
        verbose_name = "Запись расписания"
        verbose_name_plural = "Записи расписания"
        ordering = ['day_of_week', 'start_time']

    def __str__(self):
        return f"{self.title} ({self.get_day_of_week_display()})"