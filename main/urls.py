from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/stores/", include("store_api.urls", namespace="store_api")),
    path("api/profiles/", include("accounts.profiles.urls", namespace="profiles")),
    path("api/orders/", include("orders.urls", namespace="orders")),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
    path("docs/", include_docs_urls(title="TailorAPI")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("schema", get_schema_view(title="Tailor API Project", description="API for all tailor app …", version="1.0.0"), name="tailorapi-schema"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# EXTRA ADMIN CONFIGURATION
admin.site.site_header = "Tailor Admin"
admin.site.site_title = "Tailor Admin Portal"
admin.site.index_title = "Welcome to the Tailor Portal"
