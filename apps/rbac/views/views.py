from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# app/views.py
from ..tasks import add


def test_celery(request):
    for i in range(100):
        add.delay(3, 5)

    return HttpResponse("Celery works")
