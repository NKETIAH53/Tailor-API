from django.contrib import admin
from .models import StoreOwnerProfile, ClientProfile


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ["id", "pkid", "user", "gender", "phone_number"]
#     list_filter = ["gender"]
#     list_display_links = ["id", "pkid", "user"]


admin.site.register(StoreOwnerProfile)

admin.site.register(ClientProfile)
# admin.site.register(Measurement)
