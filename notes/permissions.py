from django.contrib.auth.models import User
from rest_framework import permissions


class IsOwnerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        search_result = User.objects.get(username=request.user)
        if search_result:
            return obj.author_id == search_result.id
        return False
