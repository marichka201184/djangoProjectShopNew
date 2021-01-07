from django.db import models


# Create your models here.

class ShopModel(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
  #  item_name=models.CharField(max_length=20)

    class Meta:
        db_table = 'shop'


class ItemModel(models.Model):
    name = models.CharField(max_length=10)
    price = models.CharField(max_length=20)
    shop_name = models.ForeignKey(ShopModel, on_delete=models.CASCADE, related_name='item')

    class Meta:
        db_table = 'item'