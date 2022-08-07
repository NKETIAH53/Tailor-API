from django.urls import path
from .views import StoreList,StoreDetail

app_name = 'store_api'

urlpatterns = [
    path('', StoreList.as_view(), name='listcreate'),
    path('<int:pk>/', StoreDetail.as_view(), name='detailcreate')
]
