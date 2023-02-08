from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import ProfileForm, UserForm


@login_required(login_url="/account/login")
def profile(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, instance=request.user.profile, files=request.FILES
        )

        if request.POST.get("action") == "update_profile":
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save(commit=True)
                profile_form.save(commit=True)
                messages.success(request, "User profile updated")
                return redirect("account:profile")
    return render(
        request,
        "account/profile.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
        },
    )


class ChangePassword(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("account:profile")
    success_message = "password updated successfully"
