from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from users.api.serializers import EvUserDisplaySerializer, UserProfileImageSerializer


class CurrentUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = EvUserDisplaySerializer(request.user)
        return Response(serializer.data)


class ProfileImageUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileImageSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user
        return profile_object
