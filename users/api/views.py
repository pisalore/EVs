from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from users.models import EvUser
from users.api.serializers import EvUserDisplaySerializer, RequestFormSerializer, UserProfileImageSerializer, \
    UserProfileSerializer

from users.api.permissions import IsOwnProfileOrReadOnly
from core.utils import send_request_email


class CurrentUserAPIView(APIView):

    def get(self, request):
        if not request.user.is_anonymous:
            serializer = EvUserDisplaySerializer(request.user)
            return Response(serializer.data)
        else:
            return Response(status=204)


class UserProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "username"
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]
    serializer_class = UserProfileSerializer
    queryset = EvUser.objects.all()


class ProfileImageUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileImageSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user
        return profile_object


class ContactUsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RequestFormSerializer

    def post(self, request, *args, **kwargs):
        email = {
            "user_email": request.data.get('user_email'),
            "username": request.user.username,
            "user_message": request.data.get('user_message')}

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_request_email(**email)
        return Response(data={
            "success_message": "The request has been successfully sent. We will contact you as soon as possible."})
