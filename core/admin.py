from django.contrib import admin

from .models import AreaOffice, Band, ServiceCenter


@admin.register(AreaOffice)
class AreaOfficeConfig(admin.ModelAdmin):
    list_display = ("name", "state", "technical_manager", "code")
    ordering = ("name", "state")
    radio_fields = {"state": admin.HORIZONTAL}


@admin.register(ServiceCenter)
class ServiceCenterConfig(admin.ModelAdmin):
    list_display = ("name", "area_office", "technical_supervisor")
    list_filter = ("area_office",)
    ordering = ("name", "area_office")


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ("name", "hos", "tariff")
    ordering = ("name",)
