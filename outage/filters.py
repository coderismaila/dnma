import django_filters
from core.widgets import XDSoftDatePickerInput
from .models import Outage


class OutageFilter(django_filters.FilterSet):
    min_date = django_filters.DateFilter(
        field_name="time_out",
        label="Min Date",
        lookup_expr="gte",
        widget=XDSoftDatePickerInput(),
    )
    max_date = django_filters.DateFilter(
        field_name="time_out",
        label="Max Date",
        lookup_expr="lte",
        widget=XDSoftDatePickerInput(),
    )

    class Meta:
        model = Outage
        fields = ("feeder",)
        ordering = (
            "-time_out",
            "feeder",
        )
