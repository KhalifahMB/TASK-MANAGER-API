
from rest_framework.permissions import BasePermission


class IsSuperuserOrAssignee(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.assignee == request.user
