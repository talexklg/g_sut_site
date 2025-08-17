from django.contrib import admin
from .models import ScheduleEntry

@admin.register(ScheduleEntry)
class ScheduleEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'day_of_week', 'start_time', 'end_time', 'room', 'program', 'teacher')
    list_filter = ('day_of_week', 'program', 'teacher')
    search_fields = ('title', 'description', 'room')