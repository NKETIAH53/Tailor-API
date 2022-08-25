import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.profiles.models import StoreOwnerProfile, ClientProfile


# from main.settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model

AUTH_USER_MODEL = get_user_model()

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == "STORE_OWNER":
            return StoreOwnerProfile.objects.create(user=instance)
        return ClientProfile.objects.create(user=instance)
