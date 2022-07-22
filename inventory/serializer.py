
from rest_framework import serializers
from . models import Supplier,Inventory

class SupplierReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name']


#serializer for read particuler inventory fields
class InventoryReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ['id','name','availability','supplier']

    supplier = SupplierReadSerializer()



#serializer for read all inventory fields
class InventoryDetailsReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ['id','name','description','note','stock','availability','supplier']

    supplier = SupplierReadSerializer()
