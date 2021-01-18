from django.db import models


# Create your models here.
class ItemModel(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()
    shop_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'item'
