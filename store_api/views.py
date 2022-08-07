from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, SAFE_METHODS
from .models import Store
from .serializers import StoreSerializer


class StoreOwnerWritePermissions(BasePermission):
    message = 'Only store owners can edit store information'

    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS and obj.store_owner==request.user:
            return True

        elif request.method=='GET' and obj.store_owner!=request.user:
            return True


class StoreList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Store.storeobjects.all()
    serializer_class = StoreSerializer
    
    def perform_create(self, serializer):
        serializer.save(store_owner=self.request.user)
    

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, StoreOwnerWritePermissions]
    queryset = Store.storeobjects.all()
    serializer_class = StoreSerializer
