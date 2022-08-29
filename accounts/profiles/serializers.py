from rest_framework import serializers
from .models import StoreOwnerProfile, ClientProfile, CommonProfileFields


class StoreOwnerUpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonProfileFields
        fields = "__all__"


class ClientProfileSerializer(serializers.ModelSerializer):
    model = ClientProfile
    fields = "__all__"


class StoreOwnerProfileSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField(source="user.username")

    class Meta:
        model = StoreOwnerProfile
        fields = "__all__"

    def get_username(self, obj):
        return obj.user.username
