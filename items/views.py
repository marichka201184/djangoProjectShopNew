# Create your views here.
from rest_framework.generics import ListCreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.mixins import UpdateModelMixin

from items.serializers import ItemSerializer
from .models import ItemModel


class ItemApiView(ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = ItemModel.objects.all()


class ReadUpdateItemView(DestroyAPIView, UpdateModelMixin, ListAPIView):
    queryset = ItemModel.objects
    serializer_class = ItemSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class ReadShopItemView(ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        id = self.request.query_params.get('shop_name')
        qs = ItemModel.objects.all()
        if id:
            qs = qs.filter(shop_name=id)
        return qs
