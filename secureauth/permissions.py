from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role.name == 'admin')


class IsParentUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role.name == 'parent')
    
class IsTeacherUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role.name == 'teacher')
