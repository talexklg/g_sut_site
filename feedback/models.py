from django.db import models
from programs.models import Program

class EnrollmentRequest(models.Model):
    child_full_name = models.CharField(max_length=255, verbose_name="ФИО ребёнка")
    child_date_of_birth = models.DateField(verbose_name="Дата рождения ребёнка")
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Выбранная программа")
    parent_full_name = models.CharField(max_length=255, verbose_name="ФИО родителя")
    parent_contact_phone = models.CharField(max_length=20, verbose_name="Телефон родителя")
    parent_contact_email = models.EmailField(verbose_name="Email родителя")
    pfdo_certificate_number = models.CharField(max_length=50, verbose_name="Номер сертификата ПФДО")
    school = models.CharField(max_length=255, verbose_name="Школа")
    grade = models.CharField(max_length=50, verbose_name="Класс")
    school_shift = models.CharField(max_length=50, verbose_name="Смена в школе")
    message = models.TextField(blank=True, verbose_name="Дополнительное сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")

    class Meta:
        verbose_name = "Заявка на запись"
        verbose_name_plural = "Заявки на запись"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заявка от {self.parent_full_name} на {self.program.name if self.program else 'не указана'}"