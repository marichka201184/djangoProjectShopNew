from rest_framework.serializers import ModelSerializer

from shops.models import ShopModel


class ShopSerializer(ModelSerializer):
    class Meta:
        model = ShopModel
        fields = '__all__'



