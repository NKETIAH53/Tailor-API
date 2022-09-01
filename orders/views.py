from rest_framework import viewsets
from django_filters import rest_framework as filter
from rest_framework.permissions import IsAuthenticated
from .permissions import ClientOrderDeletePermissions
from .filters import OrderFilter
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated, ClientOrderDeletePermissions]
    serializer_class = OrderSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filterset_class = OrderFilter

    def get_queryset(self):
        return Order.objects.filter(client=self.request.user)

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)
