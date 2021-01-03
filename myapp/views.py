from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ShopSerializer
from .models import ShopModel


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
        id = self.request.query_params.get('id', None)
        print(id)
        start = self.request.query_params.get('start', None)
        print(start)
        qs = ShopModel.objects.all()
        if id:
            qs = qs.filter(pk=id)
        elif start:
            qs = qs.filter(name__startswith=start)
        serializer = ShopSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        f = self.request.query_params.get('filter', None)
        shop = ShopModel.objects.get(pk=f)
        data = self.request.data
        serializer = ShopSerializer(shop, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)