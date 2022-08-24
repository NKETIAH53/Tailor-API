from rest_framework import generics, filters, status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Store, Design, Branch
from .serializers import BranchSerializer, DesignSerializer, StoreSerializer, StoreDetailSerializer
from .filters import StoreFilter
from .permissions import StoreOwnerWritePermissions, BranchCreatePermission
from django_filters import rest_framework as filter


class StoreList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, StoreOwnerWritePermissions]
    queryset = Store.storeobjects.all()
    serializer_class = StoreSerializer
    filter_backends = (filter.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = StoreFilter
    search_fields = ['^store_name', '=store_owner__username']

    def perform_create(self, serializer):
        serializer.save(store_owner=self.request.user)


class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, StoreOwnerWritePermissions]
    queryset = Store.storeobjects.all()
    serializer_class = StoreDetailSerializer


class BranchViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, BranchCreatePermission]
    serializer_class = BranchSerializer

    def get_queryset(self):
        return Branch.objects.filter(store_id=self.kwargs['pk'])


class DesignViewSet(viewsets.ModelViewSet):
    serializer_class = DesignSerializer
    queryset = Design.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
