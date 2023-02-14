from math import sqrt

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import AreaOffice, Band


class StationType(models.TextChoices):
    DISTRIBUTION = "DX", "Distribution"
    TRANSMISSION = "TX", "Transmission"


class VoltageRatio(models.TextChoices):
    HIGH_VOLTAGE = "330/132", "330/132KV"
    MEDIUM_VOLTAGE = "132/33", "132/33KV"
    LOW_VOLTAGE = "33/11", "33/11KV"
    V_33_400 = "33/0.4", "33/0.4KV"
    V_11_400 = "11/0.4", "11/0.4KV"


class VoltageLevel(models.TextChoices):
    KV_33 = "33", "33KV"
    KV_11 = "11", "11KV"


class Usage(models.TextChoices):
    PUBLIC = "P", "Public"
    DEDICATED = "D", "Dedicated"


class Manned(models.TextChoices):
    MANNED = "Manned", "Manned"
    UNMANNED = "Unmanned", "Unmanned"


class VectorGroup(models.Model):
    name = models.CharField(_("name"), max_length=6)
    description = models.CharField(_("description"), max_length=25, blank=True)


class Station(models.Model):
    name = models.CharField(
        _("name"),
        max_length=100,
        unique=True,
        db_index=True,
    )
    short_name = models.CharField(_("short name"), max_length=20, null=True)
    total_capacity_kva = models.PositiveIntegerField(
        _("total capacity (kva)"), default=0
    )
    type = models.CharField(
        max_length=2, choices=StationType.choices, default=StationType.DISTRIBUTION
    )
    longitude = models.DecimalField(
        _("longitude"), max_digits=9, decimal_places=6, blank=True, null=True
    )
    latitude = models.DecimalField(
        _("latitude"), max_digits=9, decimal_places=6, blank=True, null=True
    )
    manned = models.CharField(
        _("Manned or Unmanned"),
        max_length=8,
        choices=Manned.choices,
        default=Manned.MANNED,
    )

    def __str__(self):
        return self.name


class Transformer(models.Model):
    name = models.CharField(_("name"), max_length=50)
    make = models.CharField(
        _("make"),
        max_length=50,
        blank=True,
    )
    capacity_kva = models.PositiveIntegerField(_("capacity (kva)"), default=0)
    voltage_ratio = models.CharField(
        max_length=7,
        choices=VoltageRatio.choices,
        default=VoltageRatio.LOW_VOLTAGE,
    )
    rated_current = models.CharField(
        _("rated current"),
        max_length=20,
        null=True,
        blank=True,
        help_text=_("primary & secondary current written as Ip/Is"),
        editable=False,
    )
    serial_number = models.CharField(
        _("serial number"), max_length=25, unique=True, null=True, blank=True
    )
    manufacture_year = models.DateField(null=True, blank=True)
    vector_group = models.ForeignKey(
        VectorGroup, on_delete=models.SET_NULL, null=True, blank=True
    )
    impedance = models.FloatField(_("impedance"), default=0.0)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        v_p = int(self.voltage_ratio.split("/")[0])
        v_s = int(self.voltage_ratio.split("/")[1])
        print(self.capacity_kva)

        # calculate secondary and primary current
        i_p = self.capacity_kva / (sqrt(3) * v_p)
        i_s = self.capacity_kva / (sqrt(3) * v_s)
        self.rated_current = f"{round(i_p,2)}/{round(i_s,2)}"
        print(self.rated_current)
        super().save(*args, **kwargs)


class PowerTransformer(Transformer):
    station = models.ForeignKey(
        Station, on_delete=models.SET_NULL, null=True, blank=True
    )
    source_feeder = models.ForeignKey(
        "Feeder",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Fill only for 33/11KV Injection Substation",
    )
    source_power_transformer = models.ForeignKey(
        "PowerTransformer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Fill only for 132KV Transformers",
    )

    class Meta:
        unique_together = ("name", "station")

    def __str__(self):
        return (
            self.name
            + " - "
            + str(self.capacity_kva / 1000)
            + "MVA - "
            + self.station.name
        )


class DistributionTransformer(Transformer):
    code = models.CharField(_("DT Code"), max_length=10, unique=True, db_index=True)
    source_feeder = models.ForeignKey(
        "Feeder", on_delete=models.SET_NULL, null=True, blank=True
    )
    usage = models.CharField(
        _("usage"), max_length=14, choices=Usage.choices, default=Usage.PUBLIC
    )
    longitude = models.DecimalField(
        _("longitude"), max_digits=9, decimal_places=6, blank=True
    )
    latitude = models.DecimalField(
        _("latitude"), max_digits=9, decimal_places=6, blank=True
    )
    units = models.SmallIntegerField(_("Number of Units"))


class Feeder(models.Model):
    name = models.CharField(
        _("feeder"),
        max_length=50,
        unique=True,
        db_index=True,
    )
    kaedco_code = models.CharField(
        _("kaedco code"), max_length=4, unique=True, null=False, blank=False
    )
    nerc_code = models.CharField(
        _("nerc code"), max_length=4, unique=True, null=False, blank=False
    )
    source_power_transformer = models.ForeignKey(
        PowerTransformer, on_delete=models.SET_NULL, null=True, blank=True
    )
    area_office = models.ForeignKey(AreaOffice, on_delete=models.SET_NULL, null=True)
    voltage_level = models.CharField(
        _("voltage level"), max_length=4, choices=VoltageLevel.choices
    )
    band = models.ForeignKey(
        Band, unique=False, on_delete=models.SET_NULL, null=True, blank=True
    )
    route_length = models.FloatField(_("route length"), blank=True, default=0.0)
    conductor_type = models.CharField(
        _("conductor type"), max_length=25, blank=True, null=True
    )
    conductor_cross_sectional_area_m2 = models.FloatField(
        _("conductor cross sectional area"), blank=True, null=True
    )

    def __str__(self):
        return self.name

    def clean(self) -> None:
        if self.voltage_level == "33" and self.source_power_transformer is None:
            raise ValidationError(_("33KV feeders must have a source transformer"))
