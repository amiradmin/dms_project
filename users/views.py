# users/views.py

from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .permissions import IsAdmin
from rest_framework.permissions import BasePermission
from typing import List, Type

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.

    Only authenticated users can access most actions.
    Admin-only access is enforced for create, update, partial_update, destroy, and list actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self) -> List[BasePermission]:
        """
        Assigns permissions based on the type of action.
        Admin access required for modifying or listing users.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'list']:
            permission_classes: List[Type[BasePermission]] = [permissions.IsAuthenticated, IsAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

