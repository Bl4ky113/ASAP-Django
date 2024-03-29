
from django.urls import path

from . import views

urlpatterns = (
    path('health_check', views.health_check, name="healthcheck_view"),
    path('login', views.LoginView.as_view(), name="login_view"),
    # path('auth', views.auth_user, name="auth_user_view")
)
