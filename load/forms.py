from django import forms
from core.widgets import XDSoftDateTimePickerInput


class LoadDateTimeFilterForm(forms.Form):
    date = forms.DateTimeField(
        widget=XDSoftDateTimePickerInput(),
    )
