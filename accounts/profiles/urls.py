from django.urls import path
from .views import StoreOwnersListAPIView, RetrieveUpdateProfileAPIView

# ,GetProfileAPIView
#  UpdateProfileAPIView


app_name = "profiles"

urlpatterns = [
    path("me/", RetrieveUpdateProfileAPIView.as_view(), name="view_update_profile"),
    # path("me/", GetProfileAPIView.as_view(), name="view_profile"),
    # path(
    #     "update/<str:username>/", UpdateProfileAPIView.as_view(), name="update_profile"
    # ),
    path(
        "store_owners/all/",
        StoreOwnersListAPIView.as_view(),
        name="store_owners_profile",
    ),
]
