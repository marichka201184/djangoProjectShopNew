from django.urls import path
from items.views import ItemApiView, ReadUpdateItemView, ReadShopItemView

urlpatterns = [
    path('', ItemApiView.as_view(), name="itemapiview"),
    path('/<int:id>', ReadUpdateItemView.as_view(), name="readUpdateItem"),
    path('/byStore', ReadShopItemView.as_view(), name="readShopUpdateItem")
]
