from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,CreateAPIView, ListAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import ShopSerializer
from .models import ShopModel
from users.permissions import IsSuperUser


class ReadView(ListAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ShopSerializer
    queryset = ShopModel.objects.all()


class MyApiView(CreateAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsSuperUser, IsAdminUser)
    serializer_class = ShopSerializer
    queryset = ShopModel.objects.all()


class ReadUpdateView(DestroyAPIView, UpdateModelMixin, ListCreateAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsSuperUser, IsAdminUser)
    queryset = ShopModel.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

