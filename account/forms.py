from bootstrap5.widgets import RadioSelectButtonGroup
from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"readonly": True}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"readonly": True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"readonly": True}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileForm(forms.ModelForm):
    staff_id = forms.CharField(widget=forms.TextInput(attrs={"readonly": True}))
    payroll_id = forms.CharField(widget=forms.TextInput(attrs={"readonly": True}))

    class Meta:
        model = Profile
        fields = "__all__"
        exclude = (
            "user",
            "gender",
            "station",
            "service_center",
            "area_office",
            "job_role",
            "other_job_role",
            "other_designation",
            "designation",
        )
