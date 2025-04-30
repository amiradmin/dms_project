from django.db import models
from django.contrib.auth import get_user_model
from storages.backends.s3boto3 import S3Boto3Storage

# Initialize MinIO storage
minio_storage: S3Boto3Storage = S3Boto3Storage()

# Custom user model
User = get_user_model()

class Document(models.Model):
    """
    Model representing a document uploaded by a user and stored in MinIO (S3-compatible storage).
    """
    title: models.CharField = models.CharField(max_length=255)
    file: models.FileField = models.FileField(upload_to='documents/', storage=minio_storage)
    uploaded_by: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        Return the title of the document for readable representation.
        """
        return self.title
