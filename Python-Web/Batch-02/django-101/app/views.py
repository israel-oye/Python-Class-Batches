from django.http import HttpResponse
from django.shortcuts import render

all_products = [
    {"id": 1, "name": "Laptop", "price": 1500.00, "color": 4281089616},
    {"id": 2, "name": "Smartphone", "price": 950.99, "color": 4281637083},
    {"id": 3, "name": "Tablet", "price": 599.99, "color": 4280193279},
    {"id": 4, "name": "Headphones", "price": 299.99, "color": 4293348412},
    {"id": 5, "name": "Smart Watch", "price": 399.99, "color": 4294928820},
]

# Create your views here.
def index(request):
    return HttpResponse("<h1>hello world</h1>")


def products(request):
    return render(request, 'products.html', {'products': all_products})
