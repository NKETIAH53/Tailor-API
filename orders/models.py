from django.db import models
from django.conf import settings
from store_api.models import Design, Branch

User = settings.AUTH_USER_MODEL


"""
1 user has many orders
1 order belongs to one user
1 order has only one design

"""


class Order(models.Model):
    """
    specify  validators such that only clients can create orders and not store_owners (TO DO).
    """

    client = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )
    design = models.ForeignKey(
        Design, on_delete=models.SET_NULL, null=True, related_name="order_designs"
    )
    store_branch = models.ForeignKey(
        Branch, on_delete=models.SET_NULL, null=True, related_name="store_orders"
    )

    def __str__(self):
        return f"{self.store_branch.store.store_name}'s order"
