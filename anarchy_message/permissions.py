import re
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
      if request.method in permissions.SAFE_METHODS:
        return True

      return obj.poster == request.user

# class SignedInOrReadyOnly(permissions.IsAuthenticatedOrReadOnly):
  # def has_permission(self, request, view, obj):
  #   if request.method in 'GET':
  #     return True

  #   if request.user:
  #     return True

  #   return False
      