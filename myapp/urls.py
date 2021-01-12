from django.urls import path
from .views import MyApiView, ReadUpdateView, ItemApiView, ReadUpdateItemView, ReadShopItemView

urlpatterns = [
    path('', MyApiView.as_view(), name="myapiview"),
    path('/<int:id>', ReadUpdateView.as_view(), name="readUpdate"),
    path('/item', ItemApiView.as_view(), name="itemapiview"),
    path('/item/<int:id>', ReadUpdateItemView.as_view(), name="readUpdateItem"),
    path('/item', ReadShopItemView.as_view(), name="readShopUpdateItem")
]
