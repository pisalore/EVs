import random
import string
import boto3

from evsapp import settings

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 8


def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))


def delete_related_user_files_s3(username):
    user_objects_prefix = settings.AWS_PUBLIC_MEDIA_LOCATION + '/' + username
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    objects_to_delete = []
    for file in s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME).objects.filter(Prefix=user_objects_prefix):
        objects_to_delete.append({'Key': file.key})

    bucket.delete_objects(Delete={
        'Objects': objects_to_delete
    }
    )
