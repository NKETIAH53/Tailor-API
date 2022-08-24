from django.contrib import admin
from .models import Order, OrderPayment


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'client')

admin.site.register(Order)
admin.site.register(OrderPayment)