from django.urls import path
from .views import ProgramListView, TeacherListView, ProgramDetailView, TeacherDetailView

app_name = 'programs'

urlpatterns = [
    path('', ProgramListView.as_view(), name='list'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('<int:pk>/', ProgramDetailView.as_view(), name='detail'),
]
