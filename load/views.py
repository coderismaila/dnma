from django.shortcuts import render
from django.forms import modelformset_factory

from .forms import LoadDateTimeFilterForm
from .models import Load
from asset.models import Feeder


# Create your views here.
def load_reading_view(request):
    LoadFormSet = modelformset_factory(Load, fields=("load_mw", "status"), extra=0)
    feeders = Feeder.objects.all()
    if request.method == "POST":
        form = LoadDateTimeFilterForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data["date"]

            qs = Load.objects.filter(date=date)
            return render(request, "load/index.html", {"qs": qs, "form": form})
    return render(request, "load/index.html", {"form": LoadDateTimeFilterForm()})
