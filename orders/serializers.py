from rest_framework import serializers
from .models import Order


class ClientOrderSerializer(serializers.ModelSerializer):
    # store_name = serializers.SerializerMethodField(source="store.store_name")
    design_cost = serializers.SerializerMethodField(source="design.cost")
    order_no = serializers.SerializerMethodField()
    design_name = serializers.SerializerMethodField(source="design.design.name")

    class Meta:
        model = Order
        fields = [
            "order_no",
            "store_branch",
            # "store_name",
            "design",
            "design_name",
            "design_cost",
        ]

    # depth = 1

    def get_client(self, obj):
        return obj.client.username

    # def get_store_name(self, obj):
    #     return obj.design.store_branch.store

    def get_design_cost(self, obj):
        return obj.design.cost

    def get_order_no(self, obj):
        return obj.id

    def get_design_name(self, obj):
        return obj.design.style


class StoreOrderSerializer(serializers.ModelSerializer):

    client_name = serializers.SerializerMethodField(source="client.user.username")
    client_email = serializers.SerializerMethodField(source="client.user.email")
    design_style = serializers.SerializerMethodField("get_design_style")
    design_cost = serializers.SerializerMethodField(source="design.cost")
    branch_name = serializers.SerializerMethodField("get_branch_name")

    class Meta:
        model = Order
        fields = [
            "client_name",
            "client_email",
            "branch_name",
            "design_style",
            "design_cost",
        ]

    def get_client_name(self, obj):
        return obj.client.username

    def get_design_style(self, obj):
        return obj.design.style

    def get_design_cost(self, obj):
        return obj.design.cost

    def get_client_email(self, obj):
        return obj.client.email

    def get_branch_name(self, obj):
        return obj.store_branch.branch_name
