
import json
import logging_handler

from django.views.generic.base import View
from django.http import JsonResponse, HttpResponseForbidden
from django.forms.models import model_to_dict

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required

from django.contrib.auth.models import User
from .models import Student

from django.db.utils import IntegrityError
from django.core.exceptions import PermissionDenied

class StudentView (View):
    http_method_names = ['POST']

    @csrf_exempt
    @permission_required(('asap.create_user',), raise_exception=True)
    def post (request, *args, **kwargs):
        try:
            decoded_body = request.body.decode('utf-8')
            student_data = json.loads(decoded_body)

            try:
                user = User.objects.create_user(
                    student_data['name'].replace(' ', '_') + '_' + student_data['lastname'].replace(' ', '_'),
                    student_data['email'],
                    student_data['password'],
                    first_name=student_data['name'],
                    last_name=student_data['lastname'],
                )

                user.groups.set(["student"])

            except IntegrityError as err:
                log_instance.critical(str(type(err)) + ' ; ' + str(err))
                return JsonResponse(
                    {
                        "error": "ERROR CREATING USER: " + str(err),
                        "code": 200-3
                    },
                    status=400
                )

            del student_data['password']

            user.save()

            try:
                student = Student.objects.create(
                    userKey=user,
                    active=student_data['active'],
                    age=student_data['age'],
                    semester=student_data['semester'],
                    major=student_data['major']
                )
            except Exception as err:
               log_instance.critical(str(type(err)) + ' ; ' + str(err))
               return JsonResponse(
                   {
                       "error": "ERROR CREATING STUDENT: " + str(err),
                       "code": 200-4
                   },
                   status=400
               )

            student.save()

            return JsonResponse(
                {
                    "content": {
                        "user":  model_to_dict(user),
                        "student": model_to_dict(student)
                    },
                    "code": 201
                },
                status=200
            )

        except Exception as err:
            logging_handler.critical_error(__name__, err)

            return JsonResponse(
                {
                    "error": "INTERNAL SERVER ERROR",
                    "code": 200-1
                },
                status=500
            )
