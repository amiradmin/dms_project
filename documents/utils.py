import boto3
from botocore.exceptions import NoCredentialsError
from django.conf import settings


def generate_presigned_url(object_name, expiration=3600):
    """
    Generate a presigned URL to share an S3 object
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        region_name='us-east-1',  # Change if needed
        use_ssl=False  # For MinIO, we disable SSL
    )

    try:
        # Generate the presigned URL to get the object
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except NoCredentialsError:
        return None

    return response

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
