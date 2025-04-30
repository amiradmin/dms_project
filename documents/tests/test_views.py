import pytest
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
def test_upload_document(django_user_model):
    user = django_user_model.objects.create_user(username='alice', password='pass123')

    client = APIClient()
    client.login(username='amir', password='Eddy@747')

    file = SimpleUploadedFile("test_file.txt", b"hello world")
    response = client.post('/api/documents/', {'file': file})

    assert response.status_code == 201


@pytest.mark.django_db
def test_upload_document(django_user_model):
    # Create a user with username 'alice'
    user = django_user_model.objects.create_user(username='alice', password='pass123')

    # Login using the correct credentials for the created user
    client = APIClient()
    client.login(username='amir', password='Eddy@747')

    file = SimpleUploadedFile("test_file.txt", b"hello world")
    response = client.post('/api/documents/', {'file': file})

    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201
