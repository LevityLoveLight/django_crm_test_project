from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name='users/login.html'
        ),
        name='login'
    ),
    path('', views.index, name='index'),
    path('vacation/', views.vacation, name='vacation'),
    path('profile/', views.profile, name='profile'),
]
