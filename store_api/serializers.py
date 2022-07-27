from rest_framework import serializers
from .models import Store, Design, DesignDetail, Media, Branch


class StoreSerializer(serializers.ModelSerializer):
    store_owner = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Store
        # fields = '__all__'
        
        fields = [
            'id',
            'store_owner',
            'store_name',
            'email',
            'about',
        ]
        depth = 3


# class DesignSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Design
#         fields = (
#             'style',
#             'description'
#         )
    
# class DesignDetailSerializer(serializers.ModelSerializer):
#     design_styles = DesignSerializer(source='Design', read_only=True)
    
#     class Meta:
#         model = DesignDetail
#         fields = (
#             'design_styles',
#             'designs',
#             'cost'
#         )
    
# class MediaSerializer(serializers.ModelSerializer):
#     design_details = DesignDetailSerializer(many=True)
    
#     class Meta:
#         model = Media
#         fields = (
#             'design_details',
#             'img_url',
#             'alt_text'
#         )

# class BranchSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Branch
#         fields = (
#             'name',
#             'location',
#             'street_name',
#             'digital_address'
#         )



# class StoreSerializer(serializers.ModelSerializer):
#     design_details = DesignDetailSerializer(many=True)
#     # store_branch = BranchSerializer(source='branch', many=True)
#     class Meta:
#         model = Store
#         fields = (
#             'id',
#             # 'store_branch',
#             'design_details',
#             'store_owner',
#             'store_name',
#             'email',
#             'about'
#         )


# class DesignSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Design
#         fields = '__all__'


# class DesignDetailSerializer(serializers.ModelSerializer):
#     design = serializers.ReadOnlyField(source='design.name')
    
#     class Meta:
#         model = DesignDetail
#         fields = (
#             'design',
#             'cost'
#         )
