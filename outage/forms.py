from datetime import datetime


from core.widgets import XDSoftDateTimePickerInput
from django import forms
from django.utils import timezone

from asset.models import Feeder

from .models import Outage


class OutageForm(forms.ModelForm):
    feeder = forms.ModelChoiceField(queryset=None, empty_label="Select Feeder")
    fault_cause = forms.CharField(widget=forms.Textarea, required=False)
    resolution = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(OutageForm, self).__init__(*args, **kwargs)
        if (
            self.user.is_staff and self.user.profile.is_hq_staff
        ) or self.user.is_superuser:
            self.fields["feeder"].queryset = Feeder.objects.all()
        elif self.user.is_staff and not self.user.profile.is_hq_staff:
            self.fields["feeder"].queryset = Feeder.objects.all().filter(
                area_office=self.user.profile.area_office
            )
        elif self.user.profile.is_dso and self.user.profile.is_hq_staff:
            self.fields["feeder"].queryset = Feeder.objects.all().filter(
                voltage_level="33"
            )
        elif self.user.profile.is_dso and not self.user.profile.is_hq_staff:
            self.fields["feeder"].queryset = Feeder.objects.all().filter(
                source_power_transformer__station=self.user.profile.station
            )

        # disable some fields during form update
        instance = getattr(self, "instance", None)
        if instance and instance.pk:
            self.fields["feeder"].widget.attrs["readonly"] = True
            self.fields["feeder"].disabled = True
            self.fields["relay_indication"].widget.attrs["readonly"] = True
            self.fields["relay_indication"].disabled = True
            self.fields["load_loss_mw"].widget.attrs["readonly"] = True
            self.fields["load_loss_mw"].disabled = True
            self.fields["time_out"].widget.attrs["readonly"] = True
            self.fields["time_out"].disabled = True

    class Meta:
        model = Outage
        exclude = ("recorded_by",)
        widgets = {
            "time_out": XDSoftDateTimePickerInput(),
            "time_in": XDSoftDateTimePickerInput(),
            "fault_cause": forms.Textarea,
            "resolution": forms.Textarea,
        }

    def clean(self):
        cleaned_data = super().clean()
        time_out = cleaned_data.get("time_out")
        time_in = cleaned_data.get("time_in")
        now = timezone.make_aware(datetime.now(), timezone.get_default_timezone())

        if time_in is not None:
            if (time_in is not None) and (time_in <= time_out):
                self.add_error("time_in", "Time in should not be before time out")
            if time_in > timezone.now():
                self.add_error("time_in", "feeder cannot be restored in the future")
            if time_out > timezone.now():
                self.add_error("time_out", "feeder cannot go out in the future")
