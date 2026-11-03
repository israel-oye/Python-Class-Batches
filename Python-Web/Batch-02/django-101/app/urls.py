from django.urls import path

from .views import books, create_book, index, product_detail, products

urlpatterns = [
    path('', index),
    path('products', products, name='products'),
    path('books', books, name='books'),
    path('new-book', create_book, name='create_book'),
    path('products/<int:id>', product_detail, name='product_detail')
]