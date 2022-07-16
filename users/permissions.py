from rest_framework import permissions


class IsPremium(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.is_premium
