from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from store_api.models import Store


User = get_user_model()


class StoreTests(APITestCase):
    
    def test_view_stores_list(self):

        url = reverse('store_api:listcreate')
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_store_by_unauthenticated_user(self):
        
        data = {
            'store_owner': 1,
            'store_name':'Grandpa',
            'email': 'a@a.com',
            'about': 'This is a test store.'
        }

        url = reverse('store_api:listcreate')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_create_and_detail_store_view_by_authenticated_user(self):

        client = APIClient()

        store_owner = User.objects.create_user(
            first_name='kojo',
            last_name='asante',
            email='a@a.com',
            username='emma', 
            password='emma1234'
        )
        
        client.login(
            email='a@a.com', 
            password='emma1234'
        )

        url = reverse('store_api:listcreate')

        data = {
            # 'store_owner': 'a',
            'store_name':'Grandpa',
            'email': 'a@a.com',
            'about': 'This is a test store.'
        }
        
        print(url)
        response = client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # View store details
        detail_url = reverse(('store_api:detailcreate'), kwargs={'pk':1})
        response = self.client.get(detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


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