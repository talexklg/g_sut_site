from django.urls import path
from .views import ScheduleListView

app_name = 'schedule'

urlpatterns = [
    path('', ScheduleListView.as_view(), name='list'),
]
