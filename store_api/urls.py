from django.urls import path
from .views import StoreList,StoreDetail

app_name = 'store_api'

urlpatterns = [
    path('stores/', StoreList.as_view(), name='listcreate'),
    path('stores/<int:pk>/', StoreDetail.as_view(), name='detailcreate')
]
