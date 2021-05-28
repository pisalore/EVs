from rest_framework.routers import SimpleRouter
from aws.api.views import AWSDocumentViewSet
router = SimpleRouter()
router.register('documents', AWSDocumentViewSet)
urlpatterns = router.urls
