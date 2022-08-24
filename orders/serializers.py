from multiprocessing.connection import Client
from xml.dom import ValidationErr
from rest_framework import serializers
from .models import  Order, OrderPayment
from store_api.models import Design


class ClientOrderSerializer(serializers.ModelSerializer):

    store_name = serializers.SerializerMethodField('get_store_name')

    class Meta:
        model = Order
        fields = [
            'id',
            'store_name',
            'store_branch',
            'order_number',
            'design',
            'fabric_source',
            'quantity',
            'total_cost'
        ]

    # def validate(self, validated_data):
    #     print(dir(validated_data))
    #     if not validated_data['order'].client == self.context['user']:
    #         raise ValidationErr('User must be a client')
    #     return validated_data

    def get_store_name(self, obj):
        return obj.store_branch.store.store_name

    # def validate_user(self, serializer):
    #     user = self.request.user
    #     if user.role != "CLIENT":
    #         raise ValidationError("Only clients can create an order.")


class StoreOrderSerializer(serializers.ModelSerializer):

    client_name = serializers.SerializerMethodField(source="client.user.username")
    client_email = serializers.SerializerMethodField(source="client.user.email")
    branch_name = serializers.SerializerMethodField("get_branch_name")

    class Meta:
        model = Order
        fields = [
            'order_number',
            "client_name",
            "client_email",
            "branch_name",
            "design",
            'fabric_source',
            "total_cost",
        ]

        # depth = 1

    def get_client_name(self, obj):
        return obj.client.username

    def get_client_email(self, obj):
        return obj.client.email

    def get_branch_name(self, obj):
        return obj.store_branch.branch_name


class OrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPayment
        fields = [
            'order',
            'amount',
            'paid_on'
        ]
        read_only_fields = ['paid_on']

    def validate(self, validated_data):  
        if not validated_data['order'].client == self.context['user']:
            raise ValidationErr('wrong user')
        return validated_data