from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "core/index.html")


@login_required()
def dashboard(request):
    return render(request, "core/dashboard.html")
