from rest_framework import serializers
from .models import Store, Design, DesignDetail, Media, Branch


# class DesignSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
#     class Meta:
#         model = Design
#         fields = ('name', 'description',)
        

# class DesignDetailSerializer(serializers.ModelSerializer):
#     design = DesignSerializer(many=True, queryset=Design.objects.all())
#     design_name = serializers.SerializerMethodField('get_design_name')

#     class Meta:
#         model = DesignDetail
#         fields = ('design', 'cost', 'design_name')


# class StoreSerializer(serializers.HyperlinkedModelSerializer):
#     design = DesignSerializer( many=True, queryset=Design.objects.all())
#     store_owner = serializers.SerializerMethodField()
#     class Meta:
#         model = Store        
#         fields = [
#             'id',
#             'store_owner',
#             'store_name',
#             'email',
#             'about',
#             'design',

#         ]
        
#         depth = 3

#     def get_store_owner(self, obj):
#         return obj.store_owner.username





class StoreSerializer(serializers.ModelSerializer):

    store_owner = serializers.SerializerMethodField()
    class Meta:
        model = Store        
        fields = [
            'id',
            'store_owner',
            'store_name',
            'email',
            'about',
            'design',
        ]

        depth = 1

    def get_store_owner(self, obj):
        return obj.store_owner.username
