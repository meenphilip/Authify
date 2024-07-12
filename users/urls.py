from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomPasswordChangeView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.user_register, name="register"),
    # change password
    path(
        "password-change/", CustomPasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html"
        ),
        name="password_change_done",
    ),
    # path("registration_done/", views.registration_done, name="registration-done"),
]
