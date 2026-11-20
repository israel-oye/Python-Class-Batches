from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from .forms import ProductForm
from .models import Order, Product, ProductCategory


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
            print(form.cleaned_data)
            form.save()
            return HttpResponse('Saved')

        _context['form'] = form


    return render(request, 'new-product.html', _context)

    # render_template('t.html', v=val)
    # render('t.html', {'v': val})


def create_product_2(req: HttpRequest):
    if req.method == 'POST':

        name = req.POST.get("name")
        price = req.POST.get("price")
        cat = req.POST.get("category")

        product = Product.objects.create(name=name, price=price, category=cat)
        product.save()

        return JsonResponse(
            data=product.to_dict()
        )
    return render(req, 'new-product-2.html')


def product_detail(req: HttpRequest, pk: int):
    p = Product.objects.get(pk=pk)
    if p is not None:
        return JsonResponse(data=p.to_dict())
    return JsonResponse(data={'message': 'Not found'})




# Model.objects.create()
# obj.save()
# obj.delete()
# Model.objects.filter()
# Model.objects.order_by('name')
# Product.objects.all().paginate(page=1, per_page=50)

# order = Order.objects.filter(id='d004-53mdmr-').first()

# p = Product.objects.filter(price__gt=50).first()
# p.order = order
# p.save()

# order.products.add(p)
# order.[related_name]_set