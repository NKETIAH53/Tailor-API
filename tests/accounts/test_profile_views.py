from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from accounts.profiles.models import StoreOwnerProfile,ClientProfile


User = get_user_model()


# class TestRetrieveUpdateProfile(APITestCase):

#     def setUp(self):
#         self.client1 = StoreOwnerProfile.objects.create_user(
#             email="janesmith@user.com",
#             password="foo",
#             username="janesmith",
#             first_name="jane",
#             last_name="smith",
#             role='CL',
#             country='GH',
#             street='102 Ave',
#             house_number='GUE18E',
#             region='Accra',
#             city='Accra',
#             digital_address='AO-345-3454',
#             phone_number='0244673783',
#             about_me='I dont know.',
#             gender='M'
#         )

#         self.profile_url = reverse('profiles:view_update_profile')

#     def test_profile_retrieve(self):
#         response = self.client.get(self.profile_url, format='json')

#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)