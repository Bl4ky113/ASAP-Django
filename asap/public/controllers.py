
import json
import logging_handler

from django.http import JsonResponse
from django.views.generic.base import View

from django.contrib.auth import authenticate
from django.contrib.sessions.backends.db import SessionStore

def health_check (request):
    return JsonResponse(
        {"content": "Everything is OK :)"},
        status=200
    )

class LoginController (View):
    http_method_names = ('post',)

    def post (self, request, *args, **kwargs):
        try:
            decoded_body = request.body.decode('utf-8')
            user_login_data = json.loads(decoded_body)

            user = authenticate(
                username=user_login_data['username'],
                password=user_login_data['password']
            )

            user_hash = user.get_session_auth_hash()
            
            print(user)
            print(type(user))
            print(dir(user))

            session = SessionStore(session_key=user_hash)

            print(session)
            print(type(session))
            print(dir(session))

            return JsonResponse(
                {
                    "content": user_hash,
                },
                status=200
            )

        except Exception as err:
            logging_handler.critical_error(__name__, err)

            return JsonResponse(
                {
                    "error": "INTERNAL SERVER ERROR",
                    "code": 300-1
                },
                status=500
            )
