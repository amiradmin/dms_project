import logging
from typing import List

from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Document
from .serializers import DocumentSerializer
from users.permissions import IsAdmin, IsEditor, IsViewer
from .utils import generate_presigned_url

# Set up logger for the views module
logger = logging.getLogger(__name__)


class DocumentPagination(PageNumberPagination):
    """
    Custom pagination class for DocumentViewSet.
    Allows configurable page size via query parameter.
    """
    page_size: int = 10
    page_size_query_param: str = 'page_size'
    max_page_size: int = 100


class DocumentViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for Document objects.
    Uses different permissions based on the type of action.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes: List[type] = [IsAuthenticated]
    pagination_class = DocumentPagination

    def get_permissions(self) -> List[IsAuthenticated]:
        """
        Return the appropriate permission class depending on the action.
        """
        if self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsEditor]
        elif self.action == 'destroy':
            permission_classes = [IsAdmin]
        else:  # 'list', 'retrieve'
            permission_classes = [IsViewer]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer: DocumentSerializer) -> None:
        """
        Automatically set uploaded_by field to the currently authenticated user on creation.
        """
        serializer.save(uploaded_by=self.request.user)

    def perform_update(self, serializer: DocumentSerializer) -> None:
        """
        Optionally reassign uploaded_by field to the current user on update.
        """
        serializer.save(uploaded_by=self.request.user)


def get_presigned_url(request: HttpRequest, document_id: int) -> HttpResponse:
    """
    Return a presigned URL for the file associated with the given document ID.
    Useful for securely downloading files from S3 (MinIO).
    """
    document: Document = get_object_or_404(Document, id=document_id)

    try:
        presigned_url: str = generate_presigned_url(document.file.name)
        if presigned_url:
            return JsonResponse({"url": presigned_url})
        else:
            logger.error(f"Failed to generate presigned URL for document {document_id}")
            return JsonResponse({"error": "Could not generate presigned URL"}, status=400)

    except Exception as e:
        logger.exception(f"Error generating presigned URL for document {document_id}: {e}")
        return JsonResponse({"error": "Internal server error"}, status=500)
