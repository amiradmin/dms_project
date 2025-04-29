from django.db import models
from django.contrib.auth import get_user_model
from storages.backends.s3boto3 import S3Boto3Storage

# Initialize MinIO storage
minio_storage = S3Boto3Storage()

User = get_user_model()

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/', storage=minio_storage)  # Use MinIO storage
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
