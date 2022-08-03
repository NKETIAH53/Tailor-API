from django.contrib import admin
from .models import Profile, Address, Measurement


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "pkid", "user", "gender", "phone_number"]
    list_filter = ["gender"]
    list_display_links = ["id", "pkid", "user"]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address)
admin.site.register(Measurement)