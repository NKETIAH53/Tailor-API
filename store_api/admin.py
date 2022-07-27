from django.contrib import admin
from .models import Store, Branch,DesignDetail,Design, Media


# class DesignAdmin(admin.StackedInline):
#     model = Design
admin.site.register(Design)
admin.site.register(Store)
admin.site.register(Branch)
admin.site.register(DesignDetail)
admin.site.register(Media)

# class BranchAdmin(admin.StackedInline):
#     model = Branch
    

# class MediaAdmin(admin.StackedInline):
#     model = Media
    
# @admin.register(Store)
# class StoreAdmin(admin.ModelAdmin):
#     inlines = [BranchAdmin]
    
#     class Meta:
#         model = Store
    

# @admin.register(DesignDetail)
# class DesignDetailAdmin(admin.ModelAdmin):
#     inlines = [MediaAdmin]
    
#     class Meta:
#         model = DesignDetail

    
    
# admin.site.register(Branch)
# admin.site.register(DesignDetail)

# class MediaAdmin(admin.ModelAdmin):
#     list_display = (
#         'alt_text',
#         'created_at',
#         'updated_at',        
#     )
# admin.site.register(Media, MediaAdmin)


# class DesignStyleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'style')
# admin.site.register(DesignStyle, DesignStyleAdmin)


# class BranchAdmin(admin.StackedInline):
#     # list_display = (
#     #     'id',
#     #     'name',
#     #     'location',
#     #     'street_name',
#     #     'digital_address',
#     # )
#     model = Branch
#     extra = 1
# # admin.site.register(Branch, BranchAdmin)


# class DesignDetailAdmin(admin.StackedInline):
# #     list_display = ('id', 'style', 'cost')
# # admin.site.register(DesignDetail, DesignDetailAdmin)
#     model = DesignDetail
#     extra = 1
    

# class StoreAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'store_owner',
#         'store_name',
#         'email',
#         'status',
#         'created_at',
#         'updated_at',
        
#     )
#     inlines = [BranchAdmin, DesignDetailAdmin]
# admin.site.register(Store, StoreAdmin)

