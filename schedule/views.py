from django_filters.views import FilterView
from .models import ScheduleEntry
from .filters import ScheduleEntryFilter
from django.db.models import Case, When, IntegerField
import datetime

class ScheduleListView(FilterView):
    model = ScheduleEntry
    template_name = 'schedule/schedule_list.html'
    context_object_name = 'schedule_entries'
    filterset_class = ScheduleEntryFilter

    def get_queryset(self):
        qs = super().get_queryset()
        day_order = Case(
            When(day_of_week='MON', then=1),
            When(day_of_week='TUE', then=2),
            When(day_of_week='WED', then=3),
            When(day_of_week='THU', then=4),
            When(day_of_week='FRI', then=5),
            When(day_of_week='SAT', then=6),
            When(day_of_week='SUN', then=7),
            default=8,
            output_field=IntegerField(),
        )
        return qs.annotate(day_order=day_order).order_by('day_order', 'start_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Monday is 0 and Sunday is 6
        current_weekday = datetime.date.today().weekday()
        # Get the display name from the model's choices
        day_choices = dict(self.model.DAY_CHOICES)
        # Map Python's weekday to model's choices keys ('MON', 'TUE', etc.)
        weekday_map = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        current_day_key = weekday_map[current_weekday]
        context['current_day_display'] = day_choices.get(current_day_key)
        return context
