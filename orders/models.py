from django.db import models
from django.conf import settings
from store_api.models import Design, Branch
import uuid

User = settings.AUTH_USER_MODEL


class Order(models.Model):

    FABRIC_SOURCE_OPTIONS = (
        ('from_store', 'Store'),
        ('from_me', 'Personal')
    )

    ORDER_STATUS_CHOICES = (
        ('Received', 'Order Received',),
        ('Processing', 'Processing',),
        ('Completed', 'Completed',),
        ('Delivered', 'Delivered',),
        ('Cancelled', 'Cancelled',),
    )

    PAYMENT_STATUS_CHOICES = (
        ('Not Paid', 'Unpaid'),
        ('Part Payment', 'Part'),
        ('Full Payment', 'Processing'),
    )

    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    order_number = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    design = models.ManyToManyField(
        Design,
        related_name="order_designs"
    )
    quantity = models.DecimalField(
        max_digits=6,
        decimal_places=0,
        default=1
    )
    fabric_source = models.CharField(
        max_length=10,
        choices=FABRIC_SOURCE_OPTIONS,
        default='from_me'
    )
    store_branch = models.ForeignKey(
        Branch,
        on_delete=models.DO_NOTHING,
    )
    order_status = models.CharField(
        max_length=50,
        choices=ORDER_STATUS_CHOICES,
        default='Received'
    )
    payment_status = models.CharField(
        max_length=100,
        choices=PAYMENT_STATUS_CHOICES,
        default='Not Paid'
    )
    total_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )


class OrderPayment(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0.00
    )
    paid_on = models.DateTimeField(
        auto_now_add=True
    )
