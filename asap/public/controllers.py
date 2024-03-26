
from django.http import JsonResponse
from django.views.generic.base import View

def health_check (request):
    return JsonResponse(
        {"content": "Everything is OK :)"},
        status=200
    )

class LoginView (View):
    http_method_names = ("post",)

    def post (self, request, *arg, **kwargs):

        return JsonResponse(
            {},
            status=200
        )
