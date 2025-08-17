from django.contrib import admin
from .models import Teacher, Program

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'experience')
    search_fields = ('full_name',)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'age_group', 'is_active')
    list_filter = ('is_active', 'teacher')
    search_fields = ('name', 'teacher__full_name')