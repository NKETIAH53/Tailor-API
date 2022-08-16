from rest_framework import serializers
from .models import StoreOwnerProfile, ClientProfile, CommonProfileFields


# class ProfileSerializer(serializers.ModelSerializer):

#     username = serializers.CharField(source="user.username")
#     first_name = serializers.CharField(source="user.first_name")
#     last_name = serializers.CharField(source="user.last_name")
#     email = serializers.EmailField(source="user.email")
#     full_name = serializers.SerializerMethodField(read_only=True)


#     class Meta:
#         model = UserProfile
#         fields = [
#             "id",
#             "username",
#             "first_name",
#             "last_name",
#             "full_name",
#             "email",
#             "phone_number",
#             "profile_photo",
#             "about_me",
#             "gender",
#             # 'address',
#             # 'measurement',
#         ]

#         depth = 1

#     def get_full_name(self, obj):
#         first_name = obj.user.first_name.title()
#         last_name = obj.user.last_name.title()
#         return f"{first_name} {last_name}"

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         if instance.store_owner:
#             representation["store_owner"] = True
#         return representation


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
