from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Document model.
    Includes a custom field to return the absolute file URL.
    """
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ['id', 'title', 'file', 'file_url', 'uploaded_by', 'uploaded_at']
        read_only_fields = ['uploaded_by', 'uploaded_at']

    def get_file_url(self, obj: Document) -> str | None:
        """
        Generate an absolute file URL using the request context.

        Args:
            obj (Document): The document instance.

        Returns:
            str | None: The full URL to the file, or None if the file is not present.
        """
        request = self.context.get('request')
        if obj.file:
            url = obj.file.url
            if request:
                return request.build_absolute_uri(url)
            return url
        return None
