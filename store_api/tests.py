from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from .models import Store


class StoreTests(APITestCase):
    
    def test_view_stores(self):
    # Test for viewing all stores.(global Permission- IsAuthenticatedOrReadOnly, makes it possible for anyone to view stores irrespective of their user status)
    # 
        url = reverse('store_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_and_detail_store_view_by_authenticated_user(self):
    # Test for creating a store.(global Permission- IsAuthenticatedOrReadOnly, makes it possible for a registered user to create stores.)
    
        self.store_owner = User.objects.create_superuser(
            username='emma', 
            password='emma1234'
        )
        self.client.login(
            username=self.store_owner.username, 
            password='emma1234'
        )
        data = {
            'store_owner': 1,
            'store_name':'Grandpa',
            'email': 'a@a.com',
            'about': 'This is a test store.'
        }
        url = reverse('store_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # View store details
        detail_url = reverse(('store_api:detailcreate'), kwargs={'pk':1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_store_by_unauthenticated_user(self):
    # Test for creating a store.(global Permission- IsAuthenticatedOrReadOnly, makes it impossible for an unregistered user to create stores.)
    
        data = {
            'store_owner': 1,
            'store_name':'Grandpa',
            'email': 'a@a.com',
            'about': 'This is a test store.'
        }
        url = reverse('store_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_store_detail_update(self):
    # #    Only the authorized store owner can update the store details. 

    #     client = APIClient()
        
    #     self.store_owner= User.objects.create_user(
    #         username='emma', 
    #         password='emma1234'
    #     )

    #     test_store = Store.objects.create(store_owner=self.store_owner, store_name='Grandpa', email= 'a@a.com', about='This is a test store.', status='accepted') 
    #     print(test_store.about)

    #     client.login(
    #         username=self.store_owner.username, 
    #         password='emma1234'
    #     )

    #     url = reverse(('store_api:detailcreate'), kwargs={'pk':1})
    #     print(url)

    #     new_data = {
    #         "id": 1,
    #         "store_owner": 1,
    #         "store_name":"Grandma",
    #         "email": "a@a.com",
    #         "about": "This is a test of store update.",
    #         'detail': [],
    #     }
    #     response = client.put(url, new_data, format='json')
    #     print(response.data)
            
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
