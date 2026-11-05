from django.urls import path

from .views import create_product, index

urlpatterns = [
    path("", index, name="home"),
    path("", create_product, name="create_product"),
]
