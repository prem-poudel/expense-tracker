from rest_framework.permissions import BasePermission, SAFE_METHODS
class IsExpenseOwnerOrAdmin(BasePermission):
    """
    Custom permission to only allow owners of an expense or admins to view or edit it.
    """

    def has_object_permission(self, request, view, obj) -> bool:
        """
        Check if the requesting user is the owner of the expense or an admin.
        """
        if request.method in SAFE_METHODS:
            return True
        return (obj.owner == request.user or request.user.is_staff)

