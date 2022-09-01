from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ..factories import BranchFactory, ClientFactory, StoreOwnerFactory, StoreFactory


class TestBranch(APITestCase):
    
    def setUp(self):
        self.test_client = ClientFactory()
        self.test_store_owner = StoreOwnerFactory()
        self.test_store = StoreFactory(store_owner=self.test_store_owner)
        self.test_branch1 = BranchFactory()
        self.branch_list_create_url = reverse('store_api:branches-list', kwargs={'pk':self.test_store.id})

    def test_store_with_no_branches(self):
        response = self.client.get(self.branch_list_create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)

    def test_store_with_multiple_branches(self):
        branches = BranchFactory.create_batch(7, store=self.test_store)
        response = self.client.get(self.branch_list_create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 7)

    # def test_store_branch_delete(self):
    #     self.client.force_authenticate(user=self.test_store_owner)
    #     branch = BranchFactory.create(store=self.test_store)
    #     branch_detail_url = reverse('store_api:branches-detail', kwargs={'pk':branch.id})

    #     response = self.client.delete(branch_detail_url)
    #     print(response.data)

    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    