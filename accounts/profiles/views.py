from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission, IsAuthenticated
from .exceptions import NotYourProfile, ProfileNotFound
from .models import StoreOwnerProfile, ClientProfile
from .renderers import ProfileJSONRenderer
from .serializers import (
    StoreOwnerProfileSerializer,
    ClientProfileSerializer,
    StoreOwnerUpdateProfileSerializer,
)
from django.conf import settings


User = settings.AUTH_USER_MODEL

class ProfileAccessUpdatePermission(BasePermission):
    message = "Users can update only their profiles."

    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT"] and obj.user == request.user:
            return True


class StoreOwnersListAPIView(generics.ListAPIView):
    """
    Authenticated users can see profiles of store owners
    """

    queryset = StoreOwnerProfile.objects.all()
    serializer_class = StoreOwnerProfileSerializer
    permission_classes = [IsAuthenticated]


class ProfileRetrieveUpdateView(APIView):

    permission_classes = [IsAuthenticated, ProfileAccessUpdatePermission]
    renderer_classes = [ProfileJSONRenderer]

    def get(self, request):
        user = self.request.user
        if user.role == "CL":
            user_profile = ClientProfile.objects.get(user=user)
            serializer = ClientProfileSerializer(
                user_profile, context={"request": request}
            )
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif user.role == "SO":
            user_profile = StoreOwnerProfile.objects.get(user=user)
            serializer = StoreOwnerProfileSerializer(
                user_profile, context={"request": request}
            )
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        """
        Currently works for only StoreOwner
        """
        user = self.request.user
        try:
            if user.role == "SO":
                StoreOwnerProfile.objects.get(user=user)
            elif user.role == "CL":
                ClientProfile.objects.get(user=user)
        except:
            raise ProfileNotFound

        user_name = user.username
        if not user_name:
            raise NotYourProfile

        data = request.data
        serializer = StoreOwnerUpdateProfileSerializer(
            instance=request.user.storeownerprofile, data=data, partial=True
        )
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
