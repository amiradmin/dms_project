from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Document
from .serializers import DocumentSerializer
from users.permissions import IsAdmin, IsEditor, IsViewer
from .utils import generate_presigned_url
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import logging

# Set up logger for the views module
logger = logging.getLogger(__name__)


class DocumentPagination(PageNumberPagination):
    page_size = 10  # Set the number of items per page
    page_size_query_param = 'page_size'  # Allows clients to modify the page size with the query parameter
    max_page_size = 100  # Max number of items per page, to avoid large requests


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]  # Default, we'll control permissions per action
    pagination_class = DocumentPagination

    def get_permissions(self):
        """
        Assign different permissions based on action (view, create, update, delete)
        """
        if self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsEditor]
        elif self.action == 'destroy':
            permission_classes = [IsAdmin]
        else:  # 'list', 'retrieve'
            permission_classes = [IsViewer]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """
        Automatically set uploaded_by field to the currently authenticated user.
        """
        serializer.save(uploaded_by=self.request.user)

    def perform_update(self, serializer):
        """
        In case someone updates the document, we can also update uploaded_by if you want.
        (Optional: remove if not needed.)
        """
        serializer.save(uploaded_by=self.request.user)


def get_presigned_url(request, document_id):
    """
    View to get a presigned URL for downloading a document
    """
    document = get_object_or_404(Document, id=document_id)

    try:
        # Generate presigned URL for the document file
        presigned_url = generate_presigned_url(document.file.name)
        if presigned_url:
            return JsonResponse({"url": presigned_url})
        else:
            logger.error(f"Failed to generate presigned URL for document {document_id}")
            return JsonResponse({"error": "Could not generate presigned URL"}, status=400)

    except Exception as e:
        logger.error(f"Error generating presigned URL for document {document_id}: {e}")
        return JsonResponse({"error": "Internal server error"}, status=500)
