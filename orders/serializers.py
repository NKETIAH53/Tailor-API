from rest_framework import serializers
from .models import Order


class ClientOrderSerializer(serializers.ModelSerializer):
    store_name = serializers.SerializerMethodField(source='store.store_name')
    design_cost = serializers.SerializerMethodField(source='design.cost')
    order_no = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = [
            'order_no',
            'store',
            'store_name',
            'design',
            'design_cost',
        ]

    # depth = 1

    def get_client(self, obj):
        return obj.client.username

    def get_store_name(self, obj):
        return obj.design.store.store_name

    def get_design_cost(self, obj):
        return obj.design.cost

    def get_order_no(self, obj):
        return obj.id


class StoreOrderSerializer(serializers.ModelSerializer):
    order_id = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField(source='client.user.username')
    client_email = serializers.SerializerMethodField(source='client.user.email')
    design_cost = serializers.SerializerMethodField(source='design.cost')
    design_name = serializers.SerializerMethodField('get_design_name')

    class Meta:
        model = Order
        fields = [
            'order_id',
            'client_name',
            'client_email',
            'design',
            'design_name',
            'design_cost',
        ]

        # depth = 2

    def get_order_id(self, obj):
        return obj.id

    def get_client_name(self, obj):
        return obj.client.username

    def get_design_name(self, obj):
        return obj.design.design.name

    def get_design_cost(self, obj):
        return obj.design.cost

    def get_client_email(self, obj):
        return obj.client.email
