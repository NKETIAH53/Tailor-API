from django.urls import path
from .views import StoreOwnersListAPIView, ProfileRetrieveUpdateView


app_name = "profiles"

urlpatterns = [
    path("me/", ProfileRetrieveUpdateView.as_view(), name="view_update_profile"),
    path("store_owners/all/",
        StoreOwnersListAPIView.as_view(),
        name="store_owners_profile",
    ),
]
