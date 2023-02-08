from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.views import dashboard, home

urlpatterns = [
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
    path("account/", include("django.contrib.auth.urls")),
    path("outage/", include("outage.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Distribution Network Management"
admin.site.site_title = "DNM"
