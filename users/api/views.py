from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from users.api.serializers import EvUserDisplaySerializer


class CurrentUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = EvUserDisplaySerializer(request.user)
        return Response(serializer.data)
