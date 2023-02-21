from django.forms import DateTimeInput
from django.forms import DateInput


class XDSoftDateTimePickerInput(DateTimeInput):
    template_name = "core/widgets/xdsoft_datetimepicker.html"


class XDSoftDatePickerInput(DateInput):
    template_name = "core/widgets/xdsoft_datepicker.html"
