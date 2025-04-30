from rest_framework import serializers
from django.contrib.auth import get_user_model
from typing import Any, Dict

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model, handling serialization and user creation.

    Fields:
        - id
        - username
        - email
        - role
        - password (write-only)
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data: Dict[str, Any]) -> User:
        """
        Overridden to handle password hashing when creating a user instance.

        Args:
            validated_data: A dictionary of validated user data.

        Returns:
            A newly created User instance with a hashed password.
        """
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
