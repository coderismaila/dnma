from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = "user"


admin.site.unregister(User)

# @admin.unregister(User)
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "designation",
        "job_role",
        "area_office",
        "service_center",
        "is_staff",
    )
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    def area_office(self, obj):
        return obj.profile.area_office

    def service_center(self, obj):
        return obj.profile.service_center

    def designation(self, obj):
        return obj.profile.designation

    def job_role(self, obj):
        return obj.profile.job_role
