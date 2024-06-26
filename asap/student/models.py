from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Student (models.Model):
    userKey = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    active = models.BooleanField(
        default=False
    )
    age = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(limit_value=0)
        ]
    )
    semester = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(limit_value=1)
        ]
    )
    major = models.CharField(
        max_length=127
    )

