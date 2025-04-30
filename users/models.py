from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser to include a 'role' field.

    Roles:
        - admin: Has full permissions, typically staff.
        - editor: Can create and modify documents.
        - viewer: Can only view documents.
    """

    ROLE_CHOICES: tuple[tuple[str, str], ...] = (
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    )

    role: models.CharField = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='viewer'
    )

    def __str__(self) -> str:
        """
        Return the string representation of the user.
        """
        return f"{self.username} ({self.role})"
