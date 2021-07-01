import random
import string
import boto3
import shutil
import os
from django.core.mail import send_mail

from evsapp import settings

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 8


def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))


def delete_related_user_files_s3(username):
    user_objects_prefix = settings.AWS_PUBLIC_MEDIA_LOCATION + f'/{username}'
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    objects_to_delete = []
    for file in s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME).objects.filter(Prefix=user_objects_prefix):
        objects_to_delete.append({'Key': file.key})
    if objects_to_delete:
        bucket.delete_objects(Delete={
            'Objects': objects_to_delete
        }
        )


def delete_related_user_files_local(username):
    user_dir_path = settings.MEDIA_ROOT + f'/{username}'
    if os.path.exists(user_dir_path):
        shutil.rmtree(user_dir_path)


def send_request_email(**email):
    user_email = email.get('user_email')
    username = email.get('username')
    message = email.get('user_message')

    message_content = f'This message has been sent from: {user_email},' \
                      f' please email this in order to answer.\n' \
                      f'Message above \n' \
                      f'{message}'
    send_mail(
        f'{username} - request',
        message_content,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )
