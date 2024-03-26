
from django.urls import path

from . import controllers

urlpatterns = (
    path('health_check', controllers.health_check),
    path('login', controllers.LoginView.as_view())
)
