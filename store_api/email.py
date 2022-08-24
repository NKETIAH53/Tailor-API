# from email.message import EmailMessage
# from .models import Store
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.conf import settings
# from django.core.mail import EmailMessage
# import logging
# logger = logging.getLogger(__name__)

# # signal to indicate a newly created store has been approved


# @receiver(post_save, sender=Store)
# def store_creation_notification(sender, instance, created, **kwargs):
#     print(instance.email)
#     if created:
#         subject = 'Thank you for adding a store.'
#         message = 'Kindly contact admin on 0548392558 for further details.'
#         from_email = settings.DEFAULT_FROM_EMAIL
#         recipient = [instance.email]

#         mail = EmailMessage(
#             subject= subject, 
#             body=message, 
#             from_email=from_email,
#             to=recipient, 
#         )
#         mail.send(fail_silently=False)
