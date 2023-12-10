from django.urls import path
from n_air import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('contact', views.contact, name='contact'),
    path('products/<slug>/', views.product, name='products'),
    path('single/<int:pk>/', views.single, name='single'),
]