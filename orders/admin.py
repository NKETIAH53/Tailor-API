from django.contrib import admin
from .models import Order, OrderPayment, OrderItem


admin.site.register(Order)
admin.site.register(OrderPayment)
admin.site.register(OrderItem)
