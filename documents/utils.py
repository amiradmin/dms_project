import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from django.conf import settings
from typing import Optional
import logging

# Set up logger for this module
logger = logging.getLogger(__name__)


def generate_presigned_url(object_name: str, expiration: int = 3600) -> Optional[str]:
    """
    Generate a presigned URL to securely access an object stored in S3-compatible storage (e.g., MinIO).

    Args:
        object_name (str): The key (file path) of the object in the bucket.
        expiration (int, optional): Time in seconds for which the presigned URL is valid. Default is 3600 (1 hour).

    Returns:
        Optional[str]: The presigned URL if successful, otherwise None.
    """
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            region_name='us-east-1',  # Change if needed
            use_ssl=settings.AWS_S3_USE_SSL  # Safer to pull from settings
        )

        response = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                'Key': object_name
            },
            ExpiresIn=expiration
        )
        return response

    except NoCredentialsError:
        logger.error("AWS credentials not found. Check environment or settings.")
    except ClientError as e:
        logger.error(f"Failed to generate presigned URL: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error generating presigned URL for {object_name}: {e}")

    return None


#
# def generate_presigned_url_for_upload(object_name, expiration=3600):
#     """
#     Generate a presigned URL to upload an S3 object
#     :param object_name: string
#     :param expiration: Time in seconds for the presigned URL to remain valid
#     :return: Presigned URL as string. If error, returns None.
#     """
#     s3_client = boto3.client(
#         's3',
#         aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#         aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#         endpoint_url=settings.AWS_S3_ENDPOINT_URL,
#         region_name='us-east-1',
#         use_ssl=False
#     )
#
#     try:
#         # Generate the presigned URL to upload the object
#         response = s3_client.generate_presigned_url('put_object',
#                                                     Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
#                                                             'Key': object_name},
#                                                     ExpiresIn=expiration)
#     except NoCredentialsError:
#         return None
#
#     return response
