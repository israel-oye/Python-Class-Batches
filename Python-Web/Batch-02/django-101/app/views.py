from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import BookForm

all_products = [
    {"id": 1, "name": "Laptop", "price": 1500.00, "color": 4281089616},
    {"id": 2, "name": "Smartphone", "price": 950.99, "color": 4281637083},
    {"id": 3, "name": "Tablet", "price": 599.99, "color": 4280193279},
    {"id": 4, "name": "Headphones", "price": 299.99, "color": 4293348412},
    {"id": 5, "name": "Smart Watch", "price": 399.99, "color": 4294928820},
]

# Create your views here.
@login_required(login_url='/auth/login')
def index(request):
    return HttpResponse(f"<h1>hello {request.user.first_name}</h1>")


def products(request):
    return render(
        request, 
        'products.html', 
        {
            'products': all_products,
            'user': request.user
        }
        )


def product_detail(request, id):
    for p in all_products:
        if p['id'] == id:
            return JsonResponse(
                {
                    "success": True,
                    "message": "Success",
                    'data': p
                }
            )
    return JsonResponse(
        {
            "success": False, 
            "message": "Error. Product not found", 
        }
    )

@csrf_exempt
def books(request):
    if request.method == 'GET':
        return JsonResponse(
            data={
                "success": True,
                "message": "Success",
                "data": [
                    {
                        "author": "Chinua Achebe",
                        "available": True,
                        "id": 1,
                        "price": 3500,
                        "title": "Things Fall Apart",
                    },
                    {
                        "author": "Chimamanda Ngozi Adichie",
                        "available": False,
                        "id": 2,
                        "price": 4200,
                        "title": "Purple Hibiscus",
                    },
                ],
            }
        )
    else:
        title = request.POST.get('title')
        return JsonResponse(data={"message": "Success", "title": title, "status": True})


def create_book(request: HttpRequest):
    _context = {}

    if request.method == 'POST':
        form = BookForm(data=request.POST)

        if form.is_valid():
            print("Successfully processed form")
            print(form.cleaned_data)
            return JsonResponse(
                data=form.cleaned_data
            )

        _context['form'] = form
        
        return render(request, 'new_book.html', _context)

    form = BookForm() 
    _context['form'] = form

    return render(request, 'new_book.html', _context)


def test_email(req):
    # send_mail(
    #     subject='Dj Email Test',
    #     message="Testing testing",
    #     recipient_list=["walon59287@bcough.com",]
    # )
    msg = EmailMessage(
            subject='Dj Email Test',
            body="Testing testing",
            to=["walon59287@bcough.com",]
    )
    msg.send()
    return HttpResponse("Sent email")