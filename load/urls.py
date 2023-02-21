from django.urls import path

from .views import load_reading_view

app_name = "load"

urlpatterns = [
    path("", load_reading_view, name="index"),
]
