# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .models import Store
from .serializers import StoreSerializer
from rest_framework import generics


class StoreList(generics.ListCreateAPIView):
    queryset = Store.storeobjects.all()
    serializer_class = StoreSerializer
    

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.storeobjects.all()
    serializer_class = StoreSerializer


# @api_view(['GET', 'POST'])
# def store_list(request):
#     stores = Store.storeobjects.all()
#     serializer = StoreSerializer(stores,many=True)
#     return Response(serializer.data)