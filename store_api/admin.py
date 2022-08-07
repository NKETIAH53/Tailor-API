from django.contrib import admin
from .models import Store, Branch,DesignDetail,Design, Media


class DesignAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(Design, DesignAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'store_owner', 'store_name', 'email','status', 'created_at', 'updated_at')
    
admin.site.register(Store, StoreAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('id','store', 'branch_name', 'location')
admin.site.register(Branch, BranchAdmin)


class DesignDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'design', 'cost')
admin.site.register(DesignDetail, DesignDetailAdmin)


admin.site.register(Media)