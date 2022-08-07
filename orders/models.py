from django.db import models
from main.settings import AUTH_USER_MODEL
from store_api.models import DesignDetail, Store

User = AUTH_USER_MODEL

class Order(models.Model):
    client = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True
    )
    design = models.ForeignKey(
        DesignDetail,
        on_delete=models.SET_NULL,
        null=True,
        related_name='order_designs'
    )
    store = models.ForeignKey(
        Store,
        on_delete=models.SET_NULL,
        null=True,
        related_name='store_orders'
    )

    def __str__(self):
        return f"{self.store.store_name}'s order"