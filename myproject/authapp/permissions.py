from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'Admin'

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'Manager'

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'Customer'
