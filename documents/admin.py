from django.contrib import admin
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Document model.
    Controls how documents are displayed and filtered in the Django admin interface.
    """
    list_display: tuple[str, ...] = ('id', 'title', 'uploaded_by', 'uploaded_at', 'file')
    list_filter: tuple[str, ...] = ('uploaded_at', 'uploaded_by')
    search_fields: tuple[str, ...] = ('title', 'uploaded_by__username')
    ordering: tuple[str] = ('-uploaded_at',)
