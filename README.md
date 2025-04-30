# DMS Project

A Django-based Document Management System (DMS) that allows users to manage, upload, and organize documents efficiently.

## Features

- User authentication (Login/Logout)
- Document upload and management
- Admin dashboard
- Fully containerized with Docker
- PostgreSQL database integration

## Tech Stack

- Django (Backend Framework)
- PostgreSQL (Database)
- Docker & Docker Compose (Containerization)
- Python 3.11

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Git

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/amiradmin/dms_project.git
   cd dms_project

## Create a .env file

Create a `.env` file in the project root with the following environment variables:

```env
# Django settings
SECRET_KEY=your-secret-key
DEBUG=True  # Change to False in production
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com  # Add allowed hosts for production

# Database settings (PostgreSQL)
POSTGRES_DB=dms_db
POSTGRES_USER=dms_user
POSTGRES_PASSWORD=dms_password
POSTGRES_HOST=db  # The service name defined in your docker-compose.yml
POSTGRES_PORT=5432

# Redis settings
REDIS_HOST=redis  # The service name defined in your docker-compose.yml
REDIS_PORT=6379

# MinIO / S3 Storage Settings
AWS_ACCESS_KEY_ID=minioadmin
AWS_SECRET_ACCESS_KEY=minioadmin
AWS_STORAGE_BUCKET_NAME=dms-bucket
AWS_S3_ENDPOINT_URL=http://minio:9000
AWS_S3_USE_SSL=False
AWS_S3_VERIFY=False
AWS_QUERYSTRING_AUTH=False
```
## Start the Services

Build and start all containers using Docker Compose:

```bash
docker-compose up --build

```
## Apply Database Migrations

To apply Django database migrations, run:

```bash
docker exec -it dms_project_django_1 python manage.py migrate

```
## Create Admin Superuser

To create a Django admin account, run:

```bash
docker exec -it dms_project_django_1 python manage.py createsuperuser

```
## Usage
#### Visit http://localhost:8000 to access the application.
#### Visit http://localhost:8000/admin/ to access the Django admin panel.
#### Swagger UI: Visit http://localhost/swagger/ for interactive API documentation
