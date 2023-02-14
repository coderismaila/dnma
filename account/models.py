from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import AreaOffice, ServiceCenter


class Gender(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"


class Designation(models.TextChoices):
    CHIEF_TECHNICAL_OFFICER = "CTO", "Chief Technical Officer"
    HEAD_OF_UNIT = "HOU", "Head of Unit"
    TECHNICAL_MANAGER = "TMG", "Technical Manager"
    TECHNICAL_SUPERVISOR = "TS", "Technical Supervisor"
    TEAM_LEAD = "TL", "Team Lead"
    SUPERVISOR = "SUP", "Supervisor"
    TEAM_MEMBER = "TM", "Team Member"
    TRAINEE = "TR", "Trainee"


class JobRole(models.TextChoices):
    DISTRIBUTION_SERVICE_OFFICER = "DSO", "Distribution Service Officer"
    PROTECTION_AND_TESTING_OFFICER = "P&T", "Protection & Testing Officer"
    POWER_LINE_TECHNICIAN = "PLT", "Power Line Technician"
    POWER_SERVICE_TECHNICIAN = "PST", "Power Service Technician"
    POWER_CABLE_TECHNICIAN = "PCT", "Power Cable Technician"
    NETWORK_PLANNER = "NP", "Network Planner"
    MAINTENANCE_ENGINEER = "OME", "Maintenance Engineer"
    DATA_ANALYST = "DA", "Data Analyst"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=10, unique=True, null=True)
    payroll_id = models.CharField(max_length=10, unique=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)
    phone_number = models.CharField(
        _("phone number"), max_length=14, null=True, blank=True
    )
    personal_email = models.EmailField(
        _("personal email"), unique=True, null=True, blank=True
    )
    gender = models.CharField(
        _("gender"), max_length=1, choices=Gender.choices, default=Gender.MALE
    )
    job_role = models.CharField(
        _("job role"), max_length=3, blank=True, choices=JobRole.choices
    )
    other_job_role = models.CharField(_("other job role"), max_length=25, blank=True)
    designation = models.CharField(
        _("designation"),
        max_length=3,
        choices=Designation.choices,
        default=Designation.TEAM_MEMBER,
    )
    other_designation = models.CharField(
        _("other designation"), max_length=25, blank=True
    )
    area_office = models.ForeignKey(
        AreaOffice, on_delete=models.SET_NULL, null=True, blank=True
    )
    service_center = models.ForeignKey(
        ServiceCenter, on_delete=models.SET_NULL, null=True, blank=True
    )
    station = models.ForeignKey(
        "asset.Station", on_delete=models.SET_NULL, blank=True, null=True
    )
    is_hq_staff = models.BooleanField(_("is head office staff?"), default=False)
    is_dso = models.BooleanField(_("is dso?"), default=False)
