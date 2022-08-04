from rest_framework import serializers
from .models import Profile, Address, Measurement


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = [
            'country',
            'street',
            'house_number',
            'region', 
            'city', 
            'digital_address',
        ]


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = [

            'neck', 
            'bust', 
            'arm_length', 
            'long_sleeve',
            'bicep', 
            'wrist', 
            'torso', 
            'waist',
            'hips', 
            'waist_to_above_knee',
            'aist_to_below_knee', 
            'calf',
        ]


class ProfileSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)
    address = AddressSerializer()
    measurement = MeasurementSerializer()

    class Meta:
        model = Profile
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "phone_number",
            "profile_photo",
            "about_me",
            "gender",
            'address',
            'measurement',
        ]

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.store_owner:
            representation["store_owner"] = True
        return representation


class UpdateProfileSerializer(serializers.ModelSerializer):
    
    address = AddressSerializer()
    Measurement = MeasurementSerializer()

    class Meta:
        model = Profile
        fields = [
            "phone_number",
            "profile_photo",
            "about_me",
            'address',
            'measurement'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.store_owner:
            representation["store_owner"] = True
        return representation