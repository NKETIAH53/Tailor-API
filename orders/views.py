from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAuthenticated
from .models import Order
from .serializers import ClientOrderSerializer, StoreOrderSerializer
from store_api.models import Store
from django.core.exceptions import ValidationError


class ClientOrderReadPermissions(BasePermission):
    message = "Users can only see and delete their own orders."

    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "DELETE"] and obj.client == request.user:
            return True


class ClientOrderList(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ClientOrderSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(client=user)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != "CLIENT":
            raise ValidationError("Only clients can create an order.")

        serializer.save(client=self.request.user)


class ClientOrderDetail(generics.RetrieveDestroyAPIView):

    permission_classes = [IsAuthenticated, ClientOrderReadPermissions]
    queryset = Order.objects.all()
    serializer_class = ClientOrderSerializer


class StoreOrderList(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = StoreOrderSerializer
    # queryset = Order.objects.filter(store_branch__id)

    def get_queryset(self):
        print("------------------------")
        # store = Store.storeobjects.get(store_owner=self.request.user)
        orders = Order.objects.filter(
            store_branch__store__store_owner=self.request.user
        )
        print("-----------------------------------")
        print(orders)
        return orders


class StoreOrderDetail(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = StoreOrderSerializer
    queryset = Order.objects.all()
