from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms

from .models import Outage


class OutageForm(forms.ModelForm):
    time_out = forms.DateTimeField(widget=DateTimePickerInput)
    time_in = forms.DateTimeField(widget=DateTimePickerInput, required=False)
    fault_cause = forms.CharField(widget=forms.Textarea)
    resolution = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Outage
        exclude = ("recorded_by",)

    def __init__(self, *args, **kwargs):
        super(OutageForm, self).__init__(*args, **kwargs)
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
