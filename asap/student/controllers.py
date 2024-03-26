
from django.contrib.auth.models import User
from django.views.generic.base import View
from django.http import JsonResponse

class StudentView (View):
    http_method_names = ["post"]

    def post (self, request):
        return
