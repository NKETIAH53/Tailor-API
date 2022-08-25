from rest_framework import serializers
from .models import Store, Branch, Design, Media


class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = [
            'image',
            'alt_text',
            'is_default',
        ]


class DesignSerializer(serializers.ModelSerializer):
    design_photos = MediaSerializer(many=True, source='design_images')

    class Meta:
        model = Design
        fields = [
            'style',
            'description',
            'design_photos',
            'fabric_available',
            'price_with_store_fabric',
            'price_without_store_fabric'
        ]

    def validate(self):
        if self.fabric_available == False and self.price_with_store_fabric not in [0 or None]:
            raise serializers.ValidationError({
                'price_with_store_fabric': 'You cannot set a price if the fabric is not available'
            })


class BranchSerializer(serializers.ModelSerializer):
    # design = DesignSerializer(many=True)
    # store = serializers.SerializerMethodField()

    class Meta:
        model = Branch
        fields = [
            'id',
            'store',
            'branch_name',
            'location',
            'street_name',
            'digital_address',
            # 'design'
        ]

        # depth = 1

        # read_only_fields = ['store', 'design']

    # def get_store(self, obj):
    #     return obj.store.store_name


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = [
            'id',
            'store_name',
            'email',
            'about',
            'policy_type',
            'part_payment_percentage'
        ]

    def validate(self, policy):
        if policy['policy_type'] == 'full_payment_before_processing' and policy['part_payment_percentage'] not in [0, None]:
            raise serializers.ValidationError({
                'part_payment_percentage': 'Part payment percentage cannot be set for a store with Full payment policy'
            })
        return policy


class StoreDetailSerializer(serializers.ModelSerializer):
    store_branch = BranchSerializer(many=True)
    store_owner = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = [
            "id",
            "store_owner",
            "store_name",
            "email",
            "about",
            'policy_type',
            'part_payment_percentage',
            'store_branch',
        ]

        # depth = 1

    def get_store_owner(self, obj):
        return obj.store_owner.username
