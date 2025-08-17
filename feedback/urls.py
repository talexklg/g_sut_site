from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('enroll/', views.enrollment_form_view, name='enrollment_form'),
    path('enroll/success/', views.enrollment_success_view, name='enrollment_success'),
]