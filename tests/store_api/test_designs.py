from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ..factories import BranchFactory, ClientFactory, StoreOwnerFactory, StoreFactory, DesignFactory


class TestBranch(APITestCase):
    
    def setUp(self):
        self.test_client = ClientFactory()
        self.test_store_owner = StoreOwnerFactory()
        self.test_store = StoreFactory(store_owner=self.test_store_owner)
        self.test_branch = BranchFactory(store=self.test_store)
        self.test_design = DesignFactory()
        self.design_list_create_url = reverse('store_api:designs-list', kwargs={'pk':self.test_branch.id})

    def test_no_design_on_store_branch(self):
        response = self.client.get(self.design_list_create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)

    def test_multiple_designs_available_on_store_branch(self):
        designs = DesignFactory.create_batch(7, store_branch=self.test_branch)
        response = self.client.get(self.design_list_create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 7)

    # def test_design_detail_view(self):
    #     self.client.force_authenticate(user=self.test_client)
    #     branch = DesignFactory(store_branch=self.test_branch)
    #     response = self.client.get(self.design_list_create_url)
    #     print(response.data)

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['count'], 1)