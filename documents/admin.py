from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploaded_by', 'uploaded_at', 'file')
    list_filter = ('uploaded_at', 'uploaded_by')
    search_fields = ('title', 'uploaded_by__username')
    ordering = ('-uploaded_at',)