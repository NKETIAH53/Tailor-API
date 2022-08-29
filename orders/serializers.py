from rest_framework import serializers
from store_api.models import Design
from .models import Order, OrderItem, OrderPayment
from django.db import transaction


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            "id",
            "order",
            "design",
            "fabric_source",
            "quantity",
            "unit_cost",
            "total_item_cost",
        ]

        read_only_fields=['order']

    def validate(self, validated_data):
        fabric_source = validated_data["fabric_source"]
        quantity = validated_data["quantity"]
        design = validated_data['design']

        if fabric_source == OrderItem.FROM_ME:
            item_cost = design.price_without_store_fabric

            if item_cost != validated_data["unit_cost"]:
                raise serializers.ValidationError("wrong cost for unit item.")
            total_cost = design.price_without_store_fabric * quantity

            if total_cost != validated_data["total_item_cost"]:
                raise serializers.ValidationError("wrong cost of order")


        elif fabric_source == OrderItem.FROM_STORE:

            if not Design.fabric_available:
                raise serializers.ValidationError("Store doesnt have fabric")

            if validated_data["unit_cost"] != design.price_with_store_fabric:
                raise serializers.ValidationError("wrong cost for unit item.")
            total_cost = design.price_with_store_fabric * quantity

            if total_cost != validated_data["total_item_cost"]:
                raise serializers.ValidationError("wrong cost of order")

        return validated_data
        
class InitialOrderPayment(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=7, decimal_places=2)


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    order_items = OrderItemSerializer(many=True,write_only=True)
    payment = InitialOrderPayment(write_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "client",
            "order_items",
            "total_cost",
            "payment_status",
            "order_status",
            "ordered_on",
            "payment",
            "store_branch"
        ]

        read_only_fields = ['order_status']

    def create(self, validated_data):
        order_items = validated_data.pop("order_items")
        payment = validated_data.pop("payment")


        with transaction.atomic():
            order = Order.objects.create(**validated_data)
            print(order)
            for order_item in order_items:
                OrderItem.objects.create(order=order, **order_item)

            OrderPayment.objects.create(
                order=order,
                amount=payment["amount"]
            )

        return order


class StoreOrderSerializer(serializers.ModelSerializer):

    order_items = OrderItemSerializer(many=True)
    client_name = serializers.SerializerMethodField(source="client.user.username")
    client_email = serializers.SerializerMethodField(source="client.user.email")

    class Meta:
        model = Order
        fields = [
            "id",
            "client_name",
            "client_email",
            "order_items",
            "total_cost", 
            "payment_status",
            "order_status",
        ]
        depth = 1

    def get_client_name(self, obj):
        return obj.client.username

    def get_client_email(self, obj):
        return obj.client.email


class OrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPayment
        fields = [
            "id", 
            "order", 
            "amount", 
            "paid_on"
        ]

        read_only_fields = ["paid_on"]

    def validate(self, validated_data):
        if not validated_data['order'].client == self.request.user:
            raise serializers.ValidationError('wrong user')
        return validated_data
