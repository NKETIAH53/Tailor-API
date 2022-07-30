from .models import Store
from .serializers import StoreSerializer
from rest_framework import generics, permissions
from rest_framework.permissions import BasePermission 


class StoreOwnerWritePermissions(BasePermission):
    # Custom user permission to give authenticated user 'Write -Permissions
    message = 'Only store owners can edit store information'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.store_owner == request.user


class StoreList(generics.ListCreateAPIView):
    queryset = Store.storeobjects.all()
    serializer_class = StoreSerializer
    
    def perform_create(self, serializer):
        serializer.save(store_owner=self.request.user)
    

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [StoreOwnerWritePermissions]
    queryset = Store.storeobjects.all()
    serializer_class = StoreSerializer
    lookup_field = 'pk'
