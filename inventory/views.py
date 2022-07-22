from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Supplier, Inventory
from django.core import serializers
from .serializer import InventoryReadSerializer,InventoryDetailsReadSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



class GetInventory(APIView):
    serializer_class =InventoryReadSerializer
    def get(self, request,name=None, *args, **kwargs):
        name = self.request.query_params.get('name',None)

        if name:
            
            inventory_data = Inventory.objects.filter(name=name)#if user addd name filer then it will filter by name
        else:
            
            inventory_data = Inventory.objects.all()#access all inventory details
        return Response(InventoryReadSerializer(inventory_data,many=True, *args, **kwargs).data)
                  

get_inventory_list = GetInventory.as_view()


class GetInventoryDetails(APIView):
    serializer_class =InventoryDetailsReadSerializer
    def get(self, request,id=None,*args, **kwargs):
        id = self.kwargs.get('id')
        if id:
            inventory_data = Inventory.objects.filter(id=id)
            if inventory_data:
                inventory_data =[0]
            return render(request,'index.html',{'result':inventory_data})
                  

get_inventory_details = GetInventoryDetails.as_view()
