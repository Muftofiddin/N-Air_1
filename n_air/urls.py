from django.urls import path
from n_air import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('contact', views.contact, name='contact'),
    path('product', views.product, name='product'),
    path('single', views.single, name='single'),
]