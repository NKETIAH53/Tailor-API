from .views import OrderViewSet
from rest_framework.routers import DefaultRouter


app_name = "orders"

router = DefaultRouter()
router.register(r"", OrderViewSet, basename='orders')

urlpatterns = [

] + router.urls
