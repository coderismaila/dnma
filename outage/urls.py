from django.urls import path

from .views import (OutageDetailView, OutageListView,  # DeleteOutageView,
                    RecordOutageView, UpdateOutageView, outage_delete_view)

app_name = "outage"
urlpatterns = [
    path("", OutageListView.as_view(), name="index"),
    path("record-outage", RecordOutageView.as_view(), name="record_outage"),
    path("<int:pk>", OutageDetailView.as_view(), name="outage_detail"),
    path("update-outage/<int:pk>", UpdateOutageView.as_view(), name="update_outage"),
    # path("delete-outage/<int:pk>", DeleteOutageView.as_view(), name="delete_outage"),
    path("delete-outage/<int:pk>", outage_delete_view, name="delete_outage"),
]
