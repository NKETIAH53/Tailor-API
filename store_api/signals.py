from .models import Store
from django.dispatch import receiver
from django.db.models.signals import post_save
from store_api.tasks import store_creation_notification_task
import logging


logger = logging.getLogger(__name__)

# signal to indicate a newly created store has been approved
@receiver(post_save, sender=Store)
def store_creation_notification(sender, instance, created, **kwargs):

    if created:
        store_creation_notification_task(instance, **kwargs)
        logger.info(f"{instance}'s store created.")
