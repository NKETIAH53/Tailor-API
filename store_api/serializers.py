from rest_framework import serializers
from .models import Store, Design, DesignDetail, Media, Branch
from django.contrib.auth.models import User

class DesignSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Design
        

class DesignDetailSerializer(serializers.ModelSerializer):
    design = DesignSerializer(many=True, queryset=Design.objects.all())
    class Meta:
        model = DesignDetail
        fields = ('design', 'cost')

class StoreSerializer(serializers.ModelSerializer):
    design = DesignSerializer(read_only=True, many=True)
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
    def get_store_owner(self, obj):
        return obj.store_owner.username
 