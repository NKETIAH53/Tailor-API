from django.urls import path, include
from .views import StoreList, StoreDetail, BranchViewset
from rest_framework.routers import DefaultRouter

app_name = "store_api"

router = DefaultRouter()
router.register(r'branch', BranchViewset, basename='branches')

urlpatterns = [
    path("", StoreList.as_view(), name="listcreate"),
    path("<int:pk>/", StoreDetail.as_view(), name="detailcreate"),
    path("<int:pk>/", include(router.urls)),
] 

# urlpatterns += router.urls
'''
WORK ON DESIGN ENDPOINTS FOR THE STORES
'''