from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import ClientOrderReadDeletePermissions, PaymentCreatePermission
from .models import Order, OrderPayment
from .serializers import ClientOrderSerializer, StoreOrderSerializer, OrderPaymentSerializer


class ClientOrderList(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ClientOrderSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(client=user)
        return queryset

    # def get_serializer_context(self):
    #     return {'user': self.request.user}


class ClientOrderDetail(generics.RetrieveDestroyAPIView):

    permission_classes = [IsAuthenticated, ClientOrderReadDeletePermissions]
    queryset = Order.objects.all()
    serializer_class = ClientOrderSerializer


class StoreOrderList(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = StoreOrderSerializer

    def get_queryset(self):
        print("------------------------")
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


class OrderPaymentAPIView(generics.ListCreateAPIView):
    serializer_class = OrderPaymentSerializer
    permission_classes = [IsAuthenticated]
    # queryset = OrderPayment.objects.all()

    def get_serializer_context(self):
        return {'user': self.request.user}

    def get_queryset(self):
        user = self.request.user
        queryset = OrderPayment.objects.filter(order_id=user.pk)
        return queryset
