from django.views.generic import ListView
from .models import ScheduleEntry

class ScheduleListView(ListView):
    model = ScheduleEntry
    template_name = 'schedule/schedule_list.html'
    context_object_name = 'schedule_entries'