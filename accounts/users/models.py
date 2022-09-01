import uuid
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Total control of user model, setting email as the unique field
    """
    STORE_OWNER = "SO"
    CLIENT = "CL"
    USER_ROLE_TYPES = (
        (STORE_OWNER, "Owner"),
        (CLIENT, 'Client')
    )

    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(verbose_name=_("Username"), max_length=200, unique=True)
    first_name = models.CharField(verbose_name=_("Firstname"), max_length=50)
    last_name = models.CharField(verbose_name=_("Lastname"), max_length=50)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    role = models.CharField(max_length=20, choices=USER_ROLE_TYPES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "role"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

