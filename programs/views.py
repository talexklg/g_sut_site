from django.views.generic import ListView, DetailView
from .models import Program, Teacher

class ProgramListView(ListView):
    model = Program
    template_name = 'programs/program_list.html'
    context_object_name = 'programs'

class TeacherListView(ListView):
    model = Teacher
    template_name = 'programs/teacher_list.html'
    context_object_name = 'teachers'

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'programs/program_detail.html'
    context_object_name = 'program'