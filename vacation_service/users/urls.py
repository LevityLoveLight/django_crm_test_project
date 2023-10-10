from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from .views import VacationDeleteView

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="users/logged_out.html"),
        name="logout",
    ),
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("vacation/", views.vacation, name="vacation"),
    path(
        "vacation/<int:pk>/delete/",
        VacationDeleteView.as_view(),
        name="vacation-delete",
    ),
]
