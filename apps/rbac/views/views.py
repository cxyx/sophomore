from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# app/views.py
from ..tasks import add
from ..serializers.menu_serializer import *
from ..serializers.organization_serializer import *
from ..serializers.permission_serializer import *
from ..serializers.role_serializer import *
from ..serializers.user_serializer import *
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from ..models import Menu

from django.contrib.auth import get_user_model

User = get_user_model()

def test_celery(request):
    for i in range(100):
        add.delay(3, 5)

    return HttpResponse("Celery works")


class MenuListView(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('name',)
    ordering_fields = ('id',)
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # filter_fields = ['']
    # search_fields = ['']
    # 部分网址用


