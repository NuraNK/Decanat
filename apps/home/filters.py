import django_filters

from .models import *


class TeachersFilter(django_filters.FilterSet):
    class Meta:
        model = Teachers
        fields = (
            'profession',
            'fakultet',
        )


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Teachers
        fields = (
            'profession',
            'fakultet'
        )
class ScheduleFilter(django_filters.FilterSet):
    class Meta:
        model = Schedule
        fields = (
            'group_num',
        )
