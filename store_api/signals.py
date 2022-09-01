from .models import Store
from django.dispatch import receiver
from django.db.models.signals import post_save
from store_api.tasks import user_store_created_email_notification_task
import logging


logger = logging.getLogger(__name__)

# signal to indicate a newly created store 
@receiver(post_save, sender=Store)
def store_creation_notification(sender, instance, created, **kwargs):

    if created:
        user_store_created_email_notification_task(instance, **kwargs)
        logger.info(f"{instance}'s store created.")
