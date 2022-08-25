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

    class StoreOwnerManager(BaseUserManager):
        def get_queryset(self, *args, **kwargs):
            results = super().get_queryset(*args, **kwargs)
            return results.filter(role="STORE_OWNER")

    class ClientManager(BaseUserManager):
        def get_queryset(self, *args, **kwargs):
            results = super().get_queryset(*args, **kwargs)
            return results.filter(role="CLIENT")

    class Role(models.TextChoices):
        STORE_OWNER = "STORE_OWNER", _("Owner")
        CLIENT = "CLIENT", _("Client")
        

    base_role = Role.STORE_OWNER

    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(verbose_name=_("Username"), max_length=200, unique=True)
    first_name = models.CharField(verbose_name=_("Firstname"), max_length=50)
    last_name = models.CharField(verbose_name=_("Lastname"), max_length=50)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    role = models.CharField(max_length=20, choices=Role.choices)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "role"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def get_short_name(self):
        return self.username


    def __str__(self):
        return self.username


class StoreOwner(User):

    base_role = User.Role.STORE_OWNER
    objects = User.StoreOwnerManager()

    class Meta:
        proxy = True


class Client(User):

    base_role = User.Role.CLIENT
    objects = User.ClientManager()

    class Meta:
        proxy = True
