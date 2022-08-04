from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from .exceptions import NotYourProfile, ProfileNotFound
from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer, UpdateProfileSerializer


# class StoreAccessUserMeasurementPermissions(BasePermission):
#     '''
#     Make user measurements available only to store in which order is placed.
#     '''
#     message = 'Store from which orders have been made can see user measurements '

#     def has_obj_permission(self, request, view, obj):
#         if request.method == SAFE_METHODS.GET:
#             return True
#         return obj. == request.user


class StoreOwnersListAPIView(generics.ListAPIView):
    '''
    Authenticated users can see profiles of store owners
    '''
    queryset = Profile.objects.filter(store_owner=True)
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]



class GetProfileAPIView(APIView):
    '''
    Authenticated user can only see own profile
    '''
    permission_classes = [IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def get(self, request):
        user = self.request.user
        user_profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(user_profile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateProfileAPIView(APIView):
    '''
    Authenticated user can only update own profile
    '''
    permission_classes = [IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]
    serializer_class = UpdateProfileSerializer

    def put(self, request, username):
        try:
            Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound

        user_name = request.user.username
        if user_name != username:
            raise NotYourProfile

        data = request.data
        serializer = UpdateProfileSerializer(
            instance=request.user.profile, data=data, partial=True
        )

        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


