from django.urls import path, include
from shops.views import MyApiView, ReadUpdateView, ReadView

urlpatterns = [
    path('', ReadView.as_view(), name="readview"),
    path('/new', MyApiView.as_view(), name="myapiview"),
    path('/<int:id>', ReadUpdateView.as_view(), name="readUpdate")
   ]
