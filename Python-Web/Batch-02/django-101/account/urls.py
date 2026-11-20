from django.urls import path

from .views import dashboard, login_user, logout_user, register

urlpatterns = [
    path('login', login_user, name='login'),
    path('register', register, name='register'),
    path('me', dashboard, name='dashboard'),
    path('logout', logout_user, name='logout')
]