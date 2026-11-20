from django.urls import path

from .views import create_product, create_product_2, index, product_detail

urlpatterns = [
    path("", index, name="home"),
    path("new-product", create_product, name="create_product"),
    path("new-product-2", create_product_2, name="create_product_2"),
    path("products/<pk>", product_detail, name="product_detail"),
]
