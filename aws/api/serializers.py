from rest_framework import serializers
from aws.models import AWSDocument


class AWSDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AWSDocument
        fields = '__all__'
