from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from account.forms import RegisterForm


# Create your views here.
def register(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            print('Form valide')
            form.save()
            # login(request, new_user)
            return redirect('login')

        else:
            print("Form Invalide", form.errors)
            return render(
                    request,
                    'register.html',
                    {'form': form},
                    status=400
                )

    form = RegisterForm()
    return render(
        request,
        'register.html',
        {'form': form}
    )


def login_user(req: HttpRequest):
    if req.user.is_authenticated:
        return redirect('dashboard')
    
    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')

        user = authenticate(req, username=email, password=password)

        if user is not None:
            login(req, user)
            return redirect('dashboard')
        else:
            return render(req, "login.html", {'error': "Invalid credentials"}, status=400)

    return render(req, 'login.html')


@login_required(login_url='/auth/login')
def dashboard(request: HttpRequest):
    ctx = {
        'user': request.user
    }

    return render(
        request,
        'dashboard.html',
        context=ctx
    )

@require_http_methods(['POST'])
def logout_user(req: HttpRequest):
    logout(req)
    return redirect('login')
