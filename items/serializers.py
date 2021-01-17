from rest_framework.serializers import ModelSerializer

from items.models import ItemModel


class ItemSerializer(ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'
