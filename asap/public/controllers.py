
import json
import logging

from django.http import JsonResponse
from django.views.generic.base import View

from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session

log_instance = logging.getLogger(__name__)

def health_check (request):
    return JsonResponse(
        {"content": "Everything is OK :)"},
        status=200
    )

class LoginView (View):
    http_method_names = ('post',)

    def post (request, *arg, **kwargs):
        try:
            if (request.method != 'POST'):
                print(request.method)
                return JsonResponse(
                    {
                        "error": "INVALID METHOD",
                        "code": 300-2  
                    },
                    status=405
                )

            decoded_body = request.body.decode('utf-8')
            user_login_data = json.loads(decoded_body)

            user = authenticate(
                username=user_login_data['username'],
                password=user_login_data['password']
            )

            user_hash = user.get_session_auth_hash()

            print(dir(Session.objects.get(session_key=user_hash)))
            # session = Session.objects.get(session_key=user_hash)
            # print(dir(session))

            return JsonResponse(
                {
                    "content": user_hash,
                },
                status=200
            )

        except Exception as err:
            log_instance.critical(str(type(err)) + ' ; ' + str(err))
            return JsonResponse(
                {
                    "error": str(err),
                    "code": 300-1
                },
                status=500
            )
