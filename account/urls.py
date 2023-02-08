from django.urls import path

from .views import ChangePassword, profile

app_name = "account"

urlpatterns = [
    path(
        "password_change/",
        ChangePassword.as_view(template_name="registration/password_change_form.html"),
        name="password_change",
    ),
    path("profile/", profile, name="profile"),
]
