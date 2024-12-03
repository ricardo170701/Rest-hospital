from rest_framework.permissions import BasePermission


class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="doctors").exists()
