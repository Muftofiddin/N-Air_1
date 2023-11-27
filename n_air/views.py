from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    ctg = Category.objects.all()
    ctx = {
        'ctg': ctg
    }
    return render(request, 'blog/index.html', ctx)


def product(request):
    ctx = {

    }
    return render(request, 'blog/products.html', ctx)

def contact(request):
    ctx = {

    }
    return render(request, 'blog/contact.html', ctx)

def register(request):
    ctx = {

    }
    return render(request, 'blog/register.html', ctx)

def single(request):
    ctx = {

    }
    return render(request, 'blog/single.html', ctx)
