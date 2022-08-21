from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=200)                        
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)     
    inventory_quantity = models.IntegerField()
    image_link = models.CharField(max_length=500)