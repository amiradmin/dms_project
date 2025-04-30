from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from typing import Any

User = get_user_model()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender: type[User], instance: User = None, created: bool = False, **kwargs: Any) -> None:
    """
    Signal receiver that creates a Token for a newly created user.

    This ensures that every user has a token immediately after registration.
    """
    if created and instance:
        Token.objects.create(user=instance)
