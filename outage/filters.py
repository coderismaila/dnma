import django_filters
from bootstrap_datepicker_plus.widgets import DatePickerInput

from .models import Outage


class OutageFilter(django_filters.FilterSet):
    min_date = django_filters.DateFilter(
        field_name="time_out",
        label="Min Date",
        lookup_expr="gte",
        widget=DatePickerInput(),
    )
    max_date = django_filters.DateFilter(
        field_name="time_out",
        label="Max Date",
        lookup_expr="lte",
        widget=DatePickerInput(),
    )

    class Meta:
        model = Outage
        fields = ("feeder",)
        ordering = (
            "-time_out",
            "feeder",
        )
