
import json
import logging

from django.views.generic.base import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django.contrib.auth.models import User
from .models import Student

from django.db.utils import IntegrityError

log_instance = logging.getLogger(__name__)

class StudentView (View):
    http_method_names = ['POST']

    @csrf_exempt
    def post (request):
        try:
            if (request.method != 'POST'):
                return JsonResponse(
                    {
                        "error": "INVALID METHOD",
                        "code": 200-2
                    },
                    status=405
                )
            
            decoded_body = request.body.decode('utf-8')
            student_data = json.loads(decoded_body)

            try:
                user = User.objects.create_user(
                    student_data['name'].replace(' ', '_') + '_' + student_data['lastname'].replace(' ', '_'),
                    student_data['email'],
                    student_data['password'],
                    first_name=student_data['name'],
                    last_name=student_data['lastname']
                )
            except IntegrityError as err:
                log_instance.critical(str(type(err)) + ' ; ' + str(err))
                return JsonResponse(
                    {
                        "error": "ERROR CREATING USER: " + str(err),
                        "code": 200-2
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
                       "code": 200-3
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
            log_instance.critical(str(type(err)) + ' : ' + str(err))
            return JsonResponse(
                {
                    "error": str(err),
                    "code": 200-1
                },
                status=500
            )
