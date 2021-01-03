from django.db import models


# Create your models here.

class ShopModel(models.Model):
    name = models.CharField(max_length=10)
    price = models.FloatField(max_length=20)

    class Meta:
        db_table = 'shop'
