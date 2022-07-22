from django.db import models

import django
# Create your models here.

class Supplier(models.Model):
    
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'supplier'

class Inventory(models.Model):
    name = models.CharField(max_length=255, null=True,)
    description = models.CharField(max_length=255, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True, default=0)
    availability = models.BooleanField(default=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='get_supplier')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'inventory'