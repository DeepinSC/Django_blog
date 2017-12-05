from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.session.get('sessionid') is not None

    def has_object_permission(self, request, view, blog):
        if request.method in permissions.SAFE_METHODS:
            return True

