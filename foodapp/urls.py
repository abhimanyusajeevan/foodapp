from django.urls import path
from . import views

app_name='foodapp'

urlpatterns = [
path('', views.index, name='index.html'),
path('login/', views.loginpage, name='login.html'),
path('registration/', views.registration, name='registration.html'),
path('registration/registered/', views.registered, name='registered.html'),
path('login/logged/', views.logged, name='logged.html'),
path('menu/', views.menu, name='menu.html'),
path('loggedout/', views.loggedout, name='loggedout.html'),
path('cart/', views.cart, name='cart.html'),
#path('checkout/', views.checkout, name='checkout.html'),
]
