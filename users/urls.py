from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]
