from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class State(models.TextChoices):
    KADUNA = "KAD", "Kaduna"
    ZAMFARA = "ZAM", "Zamfara"
    SOKOTO = "SOK", "Sokoto"
    KEBBI = "KEB", "Kebbi"


class AreaOffice(models.Model):
    name = models.CharField(
        _("area office"),
        max_length=25,
        blank=False,
        unique=True,
        error_messages={
            "unique": _("name already assigned to another area office"),
        },
    )
    code = models.CharField(
        _("area office code"),
        max_length=3,
        unique=True,
        help_text=_("required a 3 characters uniqe code"),
        error_messages={
            "unique": _("code already assigned to another area office"),
        },
    )
    technical_manager = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    state = models.CharField(
        _("state"), max_length=7, blank=True, choices=State.choices
    )

    def __str__(self):
        return self.name


class ServiceCenter(models.Model):
    name = models.CharField(
        _("service center"),
        max_length=25,
        blank=False,
        unique=True,
        error_messages={
            "unique": _("name already assigned to another area office"),
        },
    )
    area_office = models.ForeignKey(AreaOffice, models.SET_NULL, null=True, blank=True)
    technical_supervisor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        if self.area_office is not None:
            return f"{self.name} - {self.area_office}"


class Band(models.Model):
    name = models.CharField(
        _("feeder band"), max_length=1, unique=True, blank=False, null=False
    )
    description = models.CharField(
        _("band description"), max_length=1, blank=True, null=True
    )
    hos = models.PositiveSmallIntegerField(
        _("hours of supply"), null=False, blank=False
    )
    tariff = models.FloatField(_("tariff rate"), null=False, blank=False)

    def __str__(self):
        return self.name
