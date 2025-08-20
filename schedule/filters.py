import django_filters
from django import forms
from .models import ScheduleEntry
from programs.models import Program, Teacher

import django_filters
from django import forms
from .models import ScheduleEntry
from programs.models import Program, Teacher

class ScheduleEntryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название занятия'})
    )
    program = django_filters.ModelChoiceFilter(
        queryset=Program.objects.all(),
        empty_label='Все программы',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    address = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Локация'})
    )
    room = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кабинет'})
    )
    teacher = django_filters.ModelChoiceFilter(
        queryset=Teacher.objects.all(),
        empty_label='Все преподаватели',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['teacher'].field.label_from_instance = lambda obj: obj.get_short_name()

    class Meta:
        model = ScheduleEntry
        fields = ['title', 'program', 'teacher', 'room', 'address']
