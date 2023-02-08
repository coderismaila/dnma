import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from .models import Outage


class OutageTable(tables.Table):
    # buttons = tables.TemplateColumn(
    #     template_name="outage/_buttons.html", verbose_name=_("Actions"), orderable=False
    # )
    feeder = tables.TemplateColumn(
        '<a href="{{ record.get_absolute_url }}">{{ record.feeder }}</a>'
    )
    time_out = tables.DateTimeColumn(
        format="d/m/Y H:i",
        attrs={"th": {"class": "text-nowrap"}, "td": {"class": "text-nowrap"}},
    )
    time_in = tables.DateTimeColumn(
        format="d/m/Y H:i",
        attrs={"th": {"class": "text-nowrap"}, "td": {"class": "text-nowrap"}},
    )
    load_loss_mw = tables.Column(
        attrs={"th": {"class": "text-nowrap"}, "td": {"class": "text-nowrap"}}
    )
    relay_indication = tables.Column(
        attrs={"th": {"class": "text-nowrap"}, "td": {"class": "text-nowrap"}}
    )
    induced_by = tables.Column(
        attrs={"th": {"class": "text-nowrap"}, "td": {"class": "text-nowrap"}}
    )
    fault_cause = tables.Column(
        attrs={
            "th": {"class": "text-nowrap"},
            "td": {"class": "text-nowrap text-break"},
        }
    )
    recorded_by = tables.Column(attrs={"th": {"class": "text-nowrap"}})
    resolution = tables.Column(attrs={"td": {"class": "text-nowrap"}})
    tcn_staff = tables.Column(attrs={"th": {"class": "text-nowrap"}})
    updated_at = tables.DateTimeColumn(
        format="d/m/Y H:i",
        attrs={"th": {"class": "text-nowrap"}, "td": {"class": "text-nowrap"}},
    )

    class Meta:
        model = Outage
        template_name = "tables/bootstrap.html"
        exclude = ("id", "timestamp")
        attrs = {
            "class": "table table-sm table-striped",
            "thead": {"class": "font-sm"},
        }
