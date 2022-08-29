from django.db import models
from django.conf import settings
from store_api.models import Design, Branch

User = settings.AUTH_USER_MODEL


class Order(models.Model):

    RECEIVED = "R"
    PROCESSING = "P"
    COMPLETED = "C"
    DELIVERED = "D"
    CANCELLED = "Cancelled"
    ORDER_STATUS_CHOICES = (
        (RECEIVED, "Order Received"),
        (PROCESSING, "Processing"),
        (COMPLETED, "Completed"),
        (DELIVERED, "Delivered"),
        (CANCELLED, "Cancelled"),
    )

    NOT_PAID = "NP"
    PART_PAYMENT = "PP"
    FULL_PAYMENT = "FP"
    PAYMENT_STATUS_CHOICES = (
        (NOT_PAID, "Unpaid"),
        (PART_PAYMENT, "Part"),
        (FULL_PAYMENT, "Processing"),
    )

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(
        max_length=100, choices=PAYMENT_STATUS_CHOICES, default=NOT_PAID
    )
    store_branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    order_status = models.CharField(
        max_length=50, choices=ORDER_STATUS_CHOICES, default=RECEIVED
    )
    ordered_on = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):

    FROM_ME = "FM"
    FROM_STORE = "FS"
    FABRIC_SOURCE_OPTIONS = ((FROM_STORE, "Store"), (FROM_ME, "Personal"))

    design = models.ForeignKey(Design, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    fabric_source = models.CharField(max_length=10, choices=FABRIC_SOURCE_OPTIONS, default=FROM_ME)
    quantity = models.IntegerField(default=1)
    unit_cost = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_item_cost = models.DecimalField(max_digits=15, decimal_places=2, default=0)


class OrderPayment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    paid_on = models.DateTimeField(auto_now_add=True)
