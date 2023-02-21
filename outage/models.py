from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from asset.models import Feeder


class OutageType(models.TextChoices):
    IN_CIRCUIT = "IN CIRCUIT", "In Circuit"
    OVERCURRENT = "OVER CURRENT", "Overcurrent"
    EARTH_FAULT = "EARTH FAULT", "Earth Fault"
    OVERCURRENT_AND_EARTH_FAULT = (
        "OVERCURRENT & EARTH FAULT",
        "Overcurrent & Earth Fault",
    )
    OUT_OF_SERVICE = "OUT OF SERVICE", "Out of Service"
    FREQUENCY_CONTROL = "FREQUENCY CONTROL", "Frequency Control"
    PLANNED_OUTAGE = "PLANNED OUTAGE", "Planned Outage"
    SYSTEM_COLLAPSE = "SYSTEM COLLAPSE", "System Collapse"


class Outage(models.Model):
    feeder = models.ForeignKey(Feeder, on_delete=models.CASCADE)
    relay_indication = models.CharField(
        _("Relay Indication"), max_length=25, choices=OutageType.choices
    )
    load_loss_mw = models.FloatField(_("Load Loss(MW)"), default=0.0)
    time_out = models.DateTimeField(_("Time Out"))
    time_in = models.DateTimeField(_("Time In"), null=True, blank=True)
    induced_by = models.CharField(
        _("Induced By"),
        max_length=6,
        choices=[("KAEDCO", "KAEDCO"), ("TCN", "TCN")],
        null=True,
        blank=True,
    )
    fault_cause = models.CharField(
        _("Fault Cause"), max_length=255, blank=True, default=""
    )
    resolution = models.CharField(
        _("Resolution"), max_length=255, blank=True, default=""
    )
    recorded_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    tcn_staff = models.CharField(
        _("Tcn Staff name"), max_length=30, null=True, blank=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (
            "-time_out",
            "feeder",
        )

    def __str__(self):
        return self.feeder.name

    def get_duration(self):
        if self.time_in:
            duration = self.time_in - self.time_out
            total_seconds = duration.total_seconds()
            return "%02d:%02d" % (
                int((total_seconds / 3600) % 3600),
                int((total_seconds / 60) % 60),
            )
        return None

    def get_response_time_hr(self):
        if self.time_in:
            duration = self.time_in - self.time_out
            total_seconds = duration.total_seconds()
            return round(total_seconds / 3600, 2)
        return None

    def get_absolute_url(self):
        return reverse("outage:outage_detail", args=[str(self.id)])
