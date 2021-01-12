from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ShopSerializer, ItemSerializer
from .models import ShopModel, ItemModel


class MyApiView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        print(data)
        serializer = ShopSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        qs = ShopModel.objects.all()
        serializer = ShopSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReadUpdateView(APIView):
    def delete(self, *args, **kwargs):
        id = kwargs.get('id')
        shop = ShopModel.objects.get(pk=id)
        shop.delete()
        return Response("ok", status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        id = kwargs.get('id')
        data = self.request.data
        instance = ShopModel.objects.get(pk=id)
        serializer = ShopSerializer(instance=instance, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class ItemApiView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        print(data)
        serializer = ItemSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        qs = ItemModel.objects.all()
        serializer = ItemSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReadUpdateItemView(APIView):
    def delete(self, *args, **kwargs):
        id = kwargs.get('id')
        item = ItemModel.objects.get(pk=id)
        item.delete()
        return Response("ok", status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        id = kwargs.get('id')
        data = self.request.data
        instance = ItemModel.objects.get(pk=id)
        serializer = ItemSerializer(instance=instance, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def get(self, *args, **kwargs):
        id = kwargs.get('id')
        print(id)
        shop_id = self.request.query_params.get('shop_name')
        qs = ItemModel.objects.all()
        if id:
            qs = qs.filter(pk=id)
        if shop_id:
            qs= qs.filter(shop_name=shop_id)
        serializer = ItemSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReadShopItemView(APIView):
    def get(self, *args, **kwargs):
        id = self.request.query_params.get('shop_name')
        print(id)
        qs = ItemModel.objects.all()
        if id:
            qs = qs.filter(shop_name=id)
        serializer = ItemSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

