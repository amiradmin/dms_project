from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for managing the CustomUser model in Django's admin panel.

    - Lists and filters users based on roles, staff, superuser, and active status.
    - Customizes the fields and permissions displayed for user creation and editing.
    """

    model: CustomUser = CustomUser
    list_display: tuple[str, ...] = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter: tuple[str, ...] = ('role', 'is_staff', 'is_superuser', 'is_active')
    search_fields: tuple[str, ...] = ('username', 'email', 'first_name', 'last_name')
    ordering: tuple[str, ...] = ('username',)

    fieldsets: tuple[tuple[str, dict], ...] = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets: tuple[tuple[str, dict], ...] = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'role', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
