import pytest
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
def test_upload_document(django_user_model):
    user = django_user_model.objects.create_user(username='alice', password='pass123')

    client = APIClient()
    client.login(username='alice', password='pass123')

    file = SimpleUploadedFile("file.txt", b"hello world")
    response = client.post('/api/documents/upload/', {'file': file})

    assert response.status_code == 201