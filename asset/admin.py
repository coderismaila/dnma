from django.contrib import admin

from mixins.export_csv_mixins import ExportCsvMixin

from . import models


class PowerTransformerInline(admin.StackedInline):
    model = models.PowerTransformer
    extra = 0
    radio_fields = {"voltage_ratio": admin.HORIZONTAL}


@admin.register(models.Station)
class StationConfig(admin.ModelAdmin, ExportCsvMixin):
    list_display = (
        "name",
        "total_capacity_kva",
        "type",
        "location",
        "manned",
    )
    list_filter = ("type",)
    search_fields = ("name",)
    readonly_fields = ("total_capacity_kva",)
    actions = ["export_as_csv"]
    inlines = [PowerTransformerInline]

    def location(self, obj):
        if obj.latitude is None or obj.longitude is None:
            return ""
        return str(obj.latitude) + ", " + str(obj.longitude)


@admin.register(models.PowerTransformer)
class PowerTransformerConfig(admin.ModelAdmin, ExportCsvMixin):
    list_display = (
        "station",
        "name",
        "make",
        "serial_number",
        "capacity_kva",
        "voltage_ratio",
        "rated_current",
        "vector_group",
        "impedance",
        "manufacture_year",
    )
    list_filter = ("station",)
    search_fields = ("station",)
    actions = ["export_as_csv"]

    def transmission_station(self, obj):
        return obj.station.name


@admin.register(models.Feeder)
class FeederConfig(admin.ModelAdmin, ExportCsvMixin):
    list_display = (
        "name",
        "area_office",
        "source_power_transformer",
        "kaedco_code",
        "band",
        "route_length",
        "conductor_type",
        "conductor_cross_sectional_area_m2",
        "voltage_level",
    )
    search_fields = ("name",)
    list_filter = ("voltage_level", "area_office")
    radio_fields = {"voltage_level": admin.HORIZONTAL}
    ordering = ("name", "area_office")
    actions = ["export_as_csv"]

    def station(self, obj):
        if obj.source_power_transformer is not None:
            return obj.source_power_transformer.station.name
        return ""


@admin.register(models.DistributionTransformer)
class DistributionTransformerConfig(admin.ModelAdmin, ExportCsvMixin):
    list_display = (
        "name",
        "make",
        "source_feeder",
        "capacity_kva",
        "voltage_ratio",
        "vector_group",
        "impedance",
        "manufacture_year",
    )
    search_fields = ("name",)
    list_filter = ("source_feeder", "source_feeder__area_office")
    actions = ["export_as_csv"]
