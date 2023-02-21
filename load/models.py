from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.urls import reverse

from asset.models import Feeder
from outage.models import OutageType


class Status(models.TextChoices):
    IN_CIRCUIT = "IN CIRCUIT", "In Circuit"
    BLACKOUT = "BLACKOUT", "Blackout"


class Grid(models.Model):
    date = models.DateTimeField(_("date"), null=False, blank=False)
    allocation_mw = models.FloatField(
        _("Allocation (MW)"), null=False, blank=False, default=0
    )
    generation_mw = models.FloatField(
        _("Generation (MW)"), null=False, blank=False, default=0
    )
    status = models.CharField(
        _("grid status"),
        max_length=15,
        choices=Status.choices,
        default=Status.IN_CIRCUIT,
    )


class Load(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    date = models.DateTimeField(_("date"), blank=False, null=False)
    feeder = models.ForeignKey(
        Feeder, on_delete=models.DO_NOTHING, null=True, blank=True, unique=False
    )
    load_mw = models.FloatField(_("load (MW)"), blank=True, null=True)

    status = models.CharField(
        _("feeder status"),
        max_length=25,
        choices=OutageType.choices,
        default=OutageType.IN_CIRCUIT,
    )

    def __str__(self) -> str:
        return f"{self.feeder.name} - {self.load_mw} at {self.date}"

    def get_absolute_url(self):
        return reverse("load_details", args=[str(self.id)])
