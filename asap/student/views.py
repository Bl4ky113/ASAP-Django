from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index (request):
    count = 0
    for i in range(10):
        count += i ** 2

    return HttpResponse(f"{count}")
