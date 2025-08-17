from django.urls import path
from .views import ProgramListView, TeacherListView, ProgramDetailView

app_name = 'programs'

urlpatterns = [
    path('', ProgramListView.as_view(), name='list'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('<int:pk>/', ProgramDetailView.as_view(), name='detail'),
]
