from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django_tables2.export.views import ExportMixin

from .filters import OutageFilter
from .forms import OutageForm
from .models import Outage
from .tables import OutageTable


# Create your views here.
class OutageListView(ExportMixin, LoginRequiredMixin, SingleTableMixin, FilterView):
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

    def get_table_data(self):
        """
        filter appropriate outages for logged in user
        """
        qs = super(OutageListView, self).get_table_data()
        user = get_user_model().objects.get(username=self.request.user)
        if (user.is_staff and user.profile.is_hq_staff) or user.is_superuser:
            return qs
        elif user.is_staff and not user.profile.is_hq_staff:
            return qs.filter(feeder__area_office=user.profile.area_office)
        elif user.profile.is_dso and user.profile.is_hq_staff:
            return qs.filter(feeder__voltage_level="33")
        elif user.profile.is_dso and not user.profile.is_hq_staff:
            return qs.filter(
                feeder__source_power_transformer__station=user.profile.station
            )


class RecordOutageView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Outage
    form_class = OutageForm
    template_name = "outage/outage_form.html"
    success_message = "outage recorded successfully"

    # pass logged in user object to form kwargs so it can be used to fetched user queryset
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(RecordOutageView, self).get_form_kwargs(*args, **kwargs)
        print(self.request.user)
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.recorded_by = self.request.user
        self.object.save()
        return HttpResponse(status=204, headers={"HX-Trigger": "outagelistchanged"})


class UpdateOutageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Outage
    form_class = OutageForm
    template_name = "outage/outage_form.html"
    success_message = "outage updated successfully"

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(UpdateOutageView, self).get_form_kwargs(*args, **kwargs)
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(status=204, headers={"HX-Trigger": "outagelistchanged"})


class OutageDetailView(LoginRequiredMixin, DetailView):
    model = Outage
    context_object_name = "outage"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_outages = Outage.objects.filter(feeder=self.object.feeder)[:5]
        context["recent_outages"] = recent_outages
        return context


@login_required()
def outage_delete_view(request, pk=None):
    try:
        obj = Outage.objects.get(pk=pk)
    except:
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not Found")
        raise Http404()
    if request.method == "DELETE":
        obj.delete()
        success_url = reverse("outage:index")
        if request.htmx:
            headers = {"HX-Redirect": success_url}
            return HttpResponse("Success", headers=headers)
        return redirect(success_url)
