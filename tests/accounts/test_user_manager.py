from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


User = get_user_model()


class TestUserAccountManager(APITestCase):
    
    def setUp(self):
        
        self.user1 = User.objects.create_user(
            email="janesmith@user.com",
            password="foo",
            username="janesmith",
            first_name="jane",
            last_name="smith"
        )
        self.user2 = User.objects.create_superuser(
            email="johndoe@user.com",
            password="bar",
            username="johndoe",
            first_name="john",
            last_name="doe"
        )

    def test_create_user(self):

        self.assertIsInstance(self.user1, User)
        self.assertFalse(self.user1.is_staff)
        self.assertFalse(self.user1.is_superuser)
        self.assertTrue(self.user1.is_active)

    def test_create_superuser(self):

        self.assertIsInstance(self.user2, User)
        self.assertTrue(self.user2.is_staff)
        self.assertTrue(self.user2.is_superuser)

    def test_raise_valueErrors_in_user_create(self):

        with self.assertRaises(ValueError):
            User.objects.create_user(
            username='',
            email='foo@bar.com',
            password='foobar',
            first_name='bob',
            last_name='james'
        )
        with self.assertRaises(ValueError):
            User.objects.create_user(
            username='bobjames',
            email='foo',
            password='foobar',
            first_name='bob',
            last_name='james'
        )
        with self.assertRaises(ValueError):
            User.objects.create_user(
            username='bobjames',
            email='foo@bar.com',
            password='foobar',
            first_name='',
            last_name='james'
        )
        with self.assertRaises(ValueError):
            User.objects.create_user(
            username='bobjames',
            email='foo@bar.com',
            password='foobar',
            first_name='bob',
            last_name=''
        )
        with self.assertRaises(ValueError):
            User.objects.create_user(
            username='bobjames',
            email='',
            password='foobar',
            first_name='bob',
            last_name='james'
        )

    def test_raise_valueErrors_in_create_superuser(self):

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
            username='bobjames',
            email='foo@bar.com',
            password='foobar',
            first_name='bob',
            last_name='james',
            is_staff='False',              
            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
            username='bobjames',
            email='foo@bar.com',
            password='foobar',
            first_name='bob',
            last_name='james',
            is_superuser='False',              
            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
            username='bobjames',
            email='foo@bar.com',
            password='',
            first_name='bob',
            last_name='james',
            
            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
            username='bobjames',
            email='',
            password='foobar',
            first_name='bob',
            last_name='james',            
            )
