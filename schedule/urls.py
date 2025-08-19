from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('', views.ScheduleListView.as_view(), name='list'),
]