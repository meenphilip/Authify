from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm


# home page
@login_required(login_url="login")
def index(request):
    return render(request, "users/index.html", {"index": "index"})


# User login view.
def user_login(request):
    # prevent logged in user from seeing login page
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
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
                    messages.success(request, "You have successfully logged in.")
                    return redirect("index")
                else:
                    messages.error(request, "Your account is disabled.")
            else:
                messages.error(request, "Invalid login credentials.")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})


# User logout view
def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
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
            messages.success(request, "You have successfully registered!")
            return render(
                request, "users/registration_done.html", {"new_user": new_user}
            )
    else:
        form = UserRegistrationForm()
    return render(request, "users/registration.html", {"form": form})


# def registration_done(request):
#     return render(request, "users/registration_done.html", {"new_user": request.user})
