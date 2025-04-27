from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Document
from .serializers import DocumentSerializer
from users.permissions import IsAdmin, IsEditor, IsViewer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]  # Default, we'll control permissions per action

    def get_permissions(self):
        """
        Assign different permissions based on action (view, create, update, delete)
        """
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsEditor]
        elif self.action == 'destroy':
            permission_classes = [IsAdmin]
        else:  # 'list', 'retrieve'
            permission_classes = [IsViewer]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
