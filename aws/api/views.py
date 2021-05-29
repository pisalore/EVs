from rest_framework import viewsets, parsers
from rest_framework.permissions import IsAuthenticated
from aws.models import AWSDocument
from aws.api.serializers import AWSDocumentSerializer
from aws.api.permissions import IsAuthorOrReadOnly


class AWSDocumentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = AWSDocument.objects.all()
    serializer_class = AWSDocumentSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'put', 'delete']
