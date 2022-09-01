from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from store_api.models import Store
import logging


logger = logging.getLogger(__name__)

User = get_user_model()


class TestStore(APITestCase):

    def setUp(self):
        self.test_store_owner = User.objects.create_user(
            first_name="kojo",
            last_name="asante",
            email="a@a.com",
            username="emma",
            password="emma1234",
            role="SO"
        )
        self.store_create_data = {
            'store_name':'Grandpa',
            'email': 'a@a.com',
            'about': 'This is a test store.',
            "policy_type":'FPBP',
            "part_payment_percentage":0,
            "status":"A"
        }
        self.store_update_data = {
            "store_name":"Grandma",
            "email":"a@a.com",
            "about":"This is an update of store object.",
            "policy_type":"PPBP",
            "part_payment_percentage":0.5,
        }

        self.store_list_create_url = reverse("store_api:list_create")
        self.store_detail_url = reverse(("store_api:detail_destroy"), kwargs={"pk":1})

    def test_view_store_list_with_no_store(self):
        response = self.client.get(self.store_list_create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)

    def test_store_list_with_one_store(self):
        test_store = Store.objects.create(
            store_owner=self.test_store_owner,
            store_name='Grandpa',
            email='a@a.com',
            about='This is a test store.',
            policy_type='FPBP',
            part_payment_percentage=0,
            status="A"
        )
        response = self.client.get(self.store_list_create_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_create_store_by_unauthorized_user(self):
        response = self.client.post(
            self.store_list_create_url,
            self.store_create_data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_store_by_authenticated_user(self):
        self.client.force_authenticate(user=self.test_store_owner)
        response = self.client.post(
            self.store_list_create_url,
            self.store_create_data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_store_detail_view_with_no_store(self):
        response = self.client.get(self.store_detail_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_store_detail_view_of_one_store(self):
        test_store = Store.objects.create(
            store_owner=self.test_store_owner,
            store_name='Grandpa',
            email= 'a@a.com',
            about='This is a test store.',
            policy_type='FPBP',
            part_payment_percentage=0,
            status="A"
        )
        store_detail_url = reverse(("store_api:detail_destroy"), kwargs={"pk":test_store.id})
        response = self.client.get(store_detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_non_existent_store_by_authenticated_user(self):
        self.client.force_authenticate(user=self.test_store_owner)
  
        response = self.client.patch(self.store_detail_url, self.store_update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_store_detail_update_by_store_owner(self):
        self.client.force_authenticate(user=self.test_store_owner)
        test_store = Store.objects.create(
            store_owner=self.test_store_owner,
            store_name='Grandpa',
            email= 'a@a.com',
            about='This is a test store.',
            policy_type='FPBP',
            part_payment_percentage=0,
            status="A"
        )
        store_detail_url = reverse(("store_api:detail_destroy"), kwargs={"pk":test_store.id})
        response = self.client.patch(store_detail_url, self.store_update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_store_by_unauthorized_user(self):
        test_store = Store.objects.create(
            store_owner=self.test_store_owner,
            store_name='Grandpa',
            email= 'a@a.com',
            about='This is a test store.',
            policy_type='FPBP',
            part_payment_percentage=0,
            status="A"
        )
        store_detail_url = reverse(("store_api:detail_destroy"), kwargs={"pk":test_store.id})
        response = self.client.delete(store_detail_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_store_by_authorized_user(self):
        self.client.force_authenticate(user=self.test_store_owner)
        test_store = Store.objects.create(
            store_owner=self.test_store_owner,
            store_name='Grandpa',
            email= 'a@a.com',
            about='This is a test store.',
            policy_type='FPBP',
            part_payment_percentage=0,
            status="A"
        )
        store_detail_url = reverse(("store_api:detail_destroy"), kwargs={"pk":test_store.id})
        response = self.client.delete(store_detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


        
