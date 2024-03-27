
from django.urls import path

from . import controllers

urlpatterns = (
    path('', controllers.StudentView.post, name="Student root"),
)
