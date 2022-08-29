from celery import shared_task
import logging
from django.core.mail import EmailMessage
from django.conf import settings


logger = logging.getLogger(__name__)


@shared_task(name="store_creation_notification_task")
def store_creation_notification_task(instance, **kwargs):
    subject = "Thank you for adding a store."
    message = "Kindly contact admin on +233000000 for further details."
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient = [instance.email]

    mail = EmailMessage(
        subject=subject,
        body=message,
        from_email=from_email,
        to=recipient,
    )
    mail.send(fail_silently=False)

    logger.info(f"{instance}'s store creation mail has been sent successfully.")
