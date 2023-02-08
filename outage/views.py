from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django_tables2.export.views import ExportMixin
from django.urls import reverse_lazy

from .filters import OutageFilter
from .forms import OutageForm
from .models import Outage
from .tables import OutageTable


# Create your views here.
class OutageListView(ExportMixin, SingleTableMixin, FilterView):
    model = Outage
    table_class = OutageTable
    template_name = "outage/index.html"
    filterset_class = OutageFilter
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            template_name = "outage/_table_partial.html"
        else:
            template_name = "outage/index.html"

        return template_name


class RecordOutageView(SuccessMessageMixin, CreateView):
    model = Outage
    form_class = OutageForm
    template_name = "outage/outage_form.html"
    success_message = "outage recorded successfully"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.recorded_by = self.request.user
        self.object.save()
        return HttpResponse(status=204, headers={"HX-Trigger": "outagelistchanged"})


class UpdateOutageView(SuccessMessageMixin, UpdateView):
    model = Outage
    form_class = OutageForm
    template_name = "outage/outage_form.html"
    success_message = "outage updated successfully"

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(status=204, headers={"HX-Trigger": "outagelistchanged"})


class OutageDetailView(DetailView):
    model = Outage
    context_object_name = "outage"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_outages = Outage.objects.filter(feeder=self.object.feeder)[:5]
        context["recent_outages"] = recent_outages
        return context


class DeleteOutageView(DeleteView):
    model = Outage
    success_url = reverse_lazy("outage:index")
