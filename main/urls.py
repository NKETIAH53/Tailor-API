from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('store_api.urls', namespace='store_api')),
    path('api/profiles/', include('accounts.profiles.urls', namespace='profiles')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# EXTRA ADMIN CONFIGURATION
admin.site.site_header = 'Store Admin'
admin.site.site_title = 'Store Admin Portal'
admin.site.index_title = 'Welcome to the Store Portal'
