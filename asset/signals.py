from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import PowerTransformer

@receiver(post_save, sender=PowerTransformer)
def update_station_capacity(sender, instance, **kwargs):
    station = instance.station
    if station:
        station.total_capacity_kva = sum(PowerTransformer.objects.filter(station=station).values_list('capacity_kva', flat=True))
        station.save()