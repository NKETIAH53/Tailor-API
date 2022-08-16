from django.contrib.auth import get_user_model

# from django.test import TestCase
from rest_framework.test import APITestCase
from accounts.profiles.models import Profile


User = get_user_model()


class UsersManagersTests(APITestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            email="normal@user.com",
            password="foo",
            username="normal",
            first_name="norm",
            last_name="mal",
        )
        self.assertEqual(user.email, "normal@user.com")
        self.assertFalse(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNotNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="normaluser.com",
                password="foo",
                username="normal",
                first_name="norm",
                last_name="mal",
            )
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="normal@user.com",
                password="foo",
                username="",
                first_name="norm",
                last_name="mal",
            )
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="normal@user.com",
                password="foo",
                username="normal",
                first_name="",
                last_name="mal",
            )
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="normal@user.com",
                password="foo",
                username="normal",
                first_name="norm",
                last_name="",
            )
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="",
                password="foo",
                username="normal",
                first_name="norm",
                last_name="mal",
            )

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email="super@user.com",
            password="foo",
            username="normal",
            first_name="norm",
            last_name="mal",
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNotNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="foo", is_superuser=False
            )
