from django.contrib import admin

from mixins.export_csv_mixins import ExportCsvMixin

from .models import Outage


@admin.register(Outage)
class OutageConfig(admin.ModelAdmin, ExportCsvMixin):
    list_display = (
        "feeder",
        "relay_indication",
        "load_loss_mw",
        "induced_by",
        "time_out",
        "time_in",
        "duration",
        "fault_cause",
        "resolution",
        "recorded_by",
        "tcn_staff",
        "timestamp",
    )
    list_filter = ("relay_indication",)
    actions = ["export_as_csv"]

    def save_model(self, request, obj, form, change):
        obj.recorded_by = request.user
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("recorded_by",)
        form = super(OutageConfig, self).get_form(request, obj, **kwargs)
        return form

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(feeder__area_office=request.user.profile.area_office)

    def duration(self, obj):
        if obj.time_in is None:
            return None
        return obj.time_in - obj.time_out
