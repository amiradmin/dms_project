from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import View


class IsAdmin(permissions.BasePermission):
    """
    Permission to allow full access for admin users.

    Admins have the ability to manage all documents, create users, assign roles,
    and perform any other admin-level actions.
    """

    def has_permission(self, request: Request, view: View) -> bool:
        """
        Check if the requesting user has full admin (staff) privileges.

        Admin users (staff) have unrestricted access to all resources and actions.

        Args:
            request (Request): The HTTP request object.
            view (View): The view that is being accessed.

        Returns:
            bool: True if the user is an admin (staff), False otherwise.
        """
        return request.user.is_staff


class IsEditor(permissions.BasePermission):
    """
    Custom permission to allow access only to users in the 'editor' group.
    """

    def has_permission(self, request: Request, view: View) -> bool:
        """
        Check if the requesting user belongs to the 'editor' group.
        """
        return request.user.groups.filter(name='editor').exists()


class IsViewer(permissions.BasePermission):
    """
    Custom permission to allow access only to users in the 'viewer' group.
    """

    def has_permission(self, request: Request, view: View) -> bool:
        """
        Check if the requesting user belongs to the 'viewer' group.
        """
        return request.user.groups.filter(name='viewer').exists()
