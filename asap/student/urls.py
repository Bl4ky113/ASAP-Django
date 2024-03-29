
from django.urls import path

from . import controllers

urlpatterns = (
    path('', controllers.StudentView.as_view(), name="Student root"),
)
