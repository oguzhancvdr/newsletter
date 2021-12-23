from rest_framework import permissions


class IsProfileOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
      if request.method in permissions.SAFE_METHODS:
          return True
      return request.user == obj.user


class IsStatusOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
      if request.method in permissions.SAFE_METHODS:
          return True
      # breakpoint()
      return request.user.profile == obj.user_profile

