from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


User = get_user_model()

class TestUserModel(APITestCase):

    def setUp(self):
        
        self.user1 = User.objects.create_user(
            email="janesmith@user.com",
            password="foo",
            username="janesmith",
            first_name="jane",
            last_name="smith"
        )

    def test_get_user_short_name(self):
        short_name = self.user1.get_short_name()
        self.assertEqual(short_name, 'janesmith')
