from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from .forms import (
    CustomPasswordChangeForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm,
)
from .forms import LoginForm, UserRegistrationForm


# home page
@login_required(login_url="login")
def index(request):
    return render(request, "users/index.html", {"index": "index"})


# User login view.
def user_login(request):
    # prevent logged in user from seeing login page
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})


# User logout view
def user_logout(request):
    logout(request)
    return redirect("login")  # Redirect to the home page or any other page


# Register user
def user_register(request):
    if request.method == "POST":
        # instantiate form
        form = UserRegistrationForm(request.POST)
        # validated data
        if form.is_valid():
            # create new user but dont save yet
            new_user = form.save(commit=False)
            # set & hash chosen password
            new_user.set_password(form.cleaned_data["password"])
            # save the user obj
            new_user.save()
            return render(
                request, "users/registration_done.html", {"new_user": new_user}
            )
    else:
        form = UserRegistrationForm()
    return render(request, "users/registration.html", {"form": form})


def registration_done(request):
    return render(request, "users/registration_done.html", {"new_user": request.user})


# Custom Password Change View
class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = "users/password_change_form.html"


# Custom Password Reset View
class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = "users/password_reset_form.html"


# Custom Password Reset View
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = "users/password_reset_confirm.html"
