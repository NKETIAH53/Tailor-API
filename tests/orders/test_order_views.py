from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ..factories import ClientFactory, OrderFactory, OrderItemFactory, OrderPayment, DesignFactory


class TestOrderViews(APITestCase):

    def setUp(self):
        self.test_client = ClientFactory()
        self.test_order_item = OrderItemFactory()
        self.test_order = OrderFactory()
        self.test_design = DesignFactory()
        self.test_order_payment = OrderPayment()
        self.test_url = reverse('orders:orders-list')

    def test_authorized_client_view_order_list(self):
        self.client.force_authenticate(user=self.test_client)
        response = self.client.get(self.test_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_client_view_order_list(self):
        # order_item = OrderItemFactory.create_batch(5, design=self.test_design, order=self.test_order )
        response = self.client.get(self.test_url)
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)