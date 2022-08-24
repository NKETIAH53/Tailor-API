from django.contrib import admin
from .models import Store, Branch, Design, Media


class DesignAdmin(admin.ModelAdmin):
    list_display = ("id", "store_branch", "style", "description", "price_with_store_fabric", 'price_without_store_fabric')


admin.site.register(Design, DesignAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "store_owner",
        "store_name",
        "email",
        "status",
        "created_at",
        "updated_at",
    )


admin.site.register(Store, StoreAdmin)


class BranchAdmin(admin.ModelAdmin):
    list_display = ("id", "store", "branch_name", "location")


admin.site.register(Branch, BranchAdmin)


admin.site.register(Media)
