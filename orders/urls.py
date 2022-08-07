from django.urls import path
from .views import ClientOrderList, ClientOrderDetail, StoreOrderList, StoreOrderDetail


app_name = 'orders'

urlpatterns = [
    path('client/', ClientOrderList.as_view(), name='clientorderlistcreate'),
    path('client/<int:pk>/', ClientOrderDetail.as_view(), name='clientorderdetail'),
    path('store/', StoreOrderList.as_view(), name='storeorderlist'),
    path('store/<int:pk>/', StoreOrderDetail.as_view(), name='storeorderdetail')
]
