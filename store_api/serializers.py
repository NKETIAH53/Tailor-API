from rest_framework import serializers
from .models import Store


class StoreSerializer(serializers.ModelSerializer):

    store_owner = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = [
            "id",
            "store_owner",
            "store_name",
            "email",
            "about",
            # 'status'
        ]

        depth = 1

    def get_store_owner(self, obj):
        return obj.store_owner.username
