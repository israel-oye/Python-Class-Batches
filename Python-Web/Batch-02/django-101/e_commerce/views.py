from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import ProductForm
from .models import Product, ProductCategory


# Create your views here.
def index(request: HttpRequest):
    return HttpResponse('hello world')


def create_product(request: HttpRequest):
    _context = {}
    form = ProductForm()
    _context['form'] = form

    if request.method == 'POST':
        form = ProductForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Saved')

        _context['form'] = form


    return render('new-product.html', _context)

    # render_template('t.html', v=val)
    # render('t.html', {'v': val})