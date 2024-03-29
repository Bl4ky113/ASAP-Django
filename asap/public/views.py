
import json

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.base import View

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse

def health_check (request):
    template = loader.get_template('public/health_check.html')
    return HttpResponse(
        template.render()
    )

class LoginView (View):
    http_method_names = ('get', 'post')

    def get (self, request, *args, **kwargs):
        template = loader.get_template('public/login_form.html')

        print(dir(request.user))

        return HttpResponse(
            template.render(
                {},
                request
            ),
        )

    def post (self, request, *args, **kwargs):
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )

        login(request, user)

        return redirect(
            reverse("login_view")
        )
