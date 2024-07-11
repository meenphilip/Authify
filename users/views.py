from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


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
