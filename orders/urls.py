from django.urls import path
from .views import ClientOrderList, ClientOrderDetail, StoreOrderList, StoreOrderDetail, OrderPaymentAPIView


app_name = "orders"

urlpatterns = [
    path("my_orders/", ClientOrderList.as_view(), name="clientorderlistcreate"),

    path("my_store_orders/", StoreOrderList.as_view(), name="storeorderlist"),

    path("my_orders/<int:pk>/", ClientOrderDetail.as_view(), name="clientorderdetail"),

    path('my_orders/<int:pk>/payments/', OrderPaymentAPIView.as_view(), name='clientpaymentlistcreate'),

    path("my_store_orders/<int:pk>/", StoreOrderDetail.as_view(), name="storeorderdetail"),
]
