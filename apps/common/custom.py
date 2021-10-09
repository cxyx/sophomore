from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user

from icecream import ic


class RbacPermission(BasePermission):

    def get_permission_from_role(self, request):
        return {}

    def has_permission(self, request, view):
        ic(request.user)
        request.user = get_user(request)
        ic(request.user)
        ic(request.user.is_authenticated)
        request_perms = self.get_permission_from_role(request)
        # if request_perms:

        return bool(request.user and request.user.is_authenticated)
