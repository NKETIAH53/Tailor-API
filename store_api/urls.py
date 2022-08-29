from django.urls import path, include
from .views import DesignViewSet, StoreList, StoreDetail, BranchViewset
from rest_framework.routers import DefaultRouter

app_name = "store_api"

router = DefaultRouter()
router.register(r"branches", BranchViewset, basename="branches")
router.register(r"designs", DesignViewSet, basename="designs")

# both branch and design endpoints have been specified on the store detail endpoint
urlpatterns = [
    path("", StoreList.as_view(), name="listcreate"),
    path("<int:pk>/", StoreDetail.as_view(), name="detailcreate"),
    path("<int:pk>/", include(router.urls)),
]
