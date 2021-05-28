from rest_framework import viewsets, parsers
from aws.models import AWSDocument
from aws.api.serializers import AWSDocumentSerializer


class AWSDocumentViewSet(viewsets.ModelViewSet):
    queryset = AWSDocument.objects.all()
    serializer_class = AWSDocumentSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']
