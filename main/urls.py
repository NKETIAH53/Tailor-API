from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('store_api.urls', namespace='store_api')),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Store Admin'
admin.site.site_title = 'Store Admin Portal'
admin.site.index_title = 'Welcome to the Store Portal'
