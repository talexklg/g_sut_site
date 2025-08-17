from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import EnrollmentRequestForm

def enrollment_form_view(request):
    if request.method == 'POST':
        form = EnrollmentRequestForm(request.POST)
        if form.is_valid():
            enrollment_request = form.save() # Save the instance to access its data

            # Prepare email content
            subject = f'Новая заявка на запись: {enrollment_request.child_full_name}'
            message = (
                f'Получена новая заявка на запись:\n\n'
                f'ФИО ребёнка: {enrollment_request.child_full_name}\n'
                f'Дата рождения ребёнка: {enrollment_request.child_date_of_birth}\n'
                f'Выбранная программа: {enrollment_request.program.name if enrollment_request.program else "Не указана"}\n'
                f'ФИО родителя: {enrollment_request.parent_full_name}\n'
                f'Телефон родителя: {enrollment_request.parent_contact_phone}\n'
                f'Email родителя: {enrollment_request.parent_contact_email}\n'
                f'Номер сертификата ПФДО: {enrollment_request.pfdo_certificate_number}\n'
                f'Школа: {enrollment_request.school}\n'
                f'Класс: {enrollment_request.grade}\n'
                f'Смена в школе: {enrollment_request.school_shift}\n'
                f'Дополнительное сообщение: {enrollment_request.message if enrollment_request.message else "Нет"}\n'
                f'Дата заявки: {enrollment_request.created_at}\n'
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.ADMIN_EMAIL]

            # Send email
            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                messages.success(request, 'Ваша заявка успешно отправлена! Уведомление отправлено администратору.')
            except Exception as e:
                messages.error(request, f'Ваша заявка отправлена, но не удалось отправить уведомление администратору: {e}')
                # Log the error for debugging
                print(f"Error sending email: {e}")

            return redirect(reverse('feedback:enrollment_success')) # Assuming a success page
    else:
        form = EnrollmentRequestForm()
    return render(request, 'feedback/enrollment_form.html', {'form': form})

def enrollment_success_view(request):
    return render(request, 'feedback/enrollment_success.html')
