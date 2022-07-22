from django.test import TestCase

# Create your tests here.
from .models import Supplier, Inventory

class APInventoryTestCase(TestCase):
    def setUp(self):
        supplier_obj = Supplier.objects.create(name="test3")
        Inventory.objects.create(name="abc",description="key",note="ydhhdy",supplier=supplier_obj)
       

    def test_inventory_api(self):
        data = Inventory.objects.get(name="abc")
        #test case to check “/inventory” url is returns "200 OK status" or not
        response = self.client.get("/inventory")    
        self.assertEqual(response.status_code, 200)

        #test case to check “/api/inventory” url is returns "200 OK status" or not
        inventoryresponse = self.client.get("/api/inventory")    
        self.assertEqual(inventoryresponse.status_code, 200)

        

    def test_inventory_url_by_id(self):
        data = Inventory.objects.get(id=1)
        #test case to check “/inventory/<id>” url is returns "200 OK status" or not
        response = self.client.get("/inventory/1")  
        self.assertEqual(response.status_code, 200)

            
        