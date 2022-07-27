from django.urls import path
from .views import StoreList,StoreDetail
# store_list

app_name = 'store_api'

urlpatterns = [
    path('stores/', StoreList.as_view(), name='listcreate'),
    # path('', store_list, name='listcreate'),
    path('stores/<int:pk>/', StoreDetail.as_view(), name='detailcreate')
]
