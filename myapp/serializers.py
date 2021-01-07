from rest_framework.serializers import ModelSerializer

from .models import ShopModel, ItemModel


class ShopSerializer(ModelSerializer):
    class Meta:
        model = ShopModel
        fields = '__all__'


class ItemSerializer(ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'
