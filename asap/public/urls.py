
from django.urls import path

from . import controllers

urlpatterns = (
    path('health_check', controllers.health_check, name='healthcheck'),
    path('login', controllers.LoginView, name='login user')
)
