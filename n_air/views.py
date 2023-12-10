import random

from django.shortcuts import render, redirect
from .models import Category, Sneakers, Buy, Advertising
from .forms import ChoiceFrom, RegisterUp, ContactForm
import random


# Create your views here.
def home(request):
    ctg = Category.objects.all()
    sneakers = Sneakers.objects.all()
    advertising = Advertising.objects.all()
    random_pk = random.choice(advertising)
    ctx = {
        'sneakers': sneakers,
        'ctg': ctg,
        'random_pk': random_pk
    }
    return render(request, 'blog/index.html', ctx)


def product(request, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    sneaker = Sneakers.objects.all().filter(type_id=category.id)
    ctx = {
        'ctg': ctg,
        'category': category,
        'sneaker': sneaker,
    }
    return render(request, 'blog/products.html', ctx)


def contact(request):
    ctg = Category.objects.all()
    forms = ContactForm()
    if request.POST:
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    ctx = {
        'ctg': ctg,
        'forms': forms
    }
    return render(request, 'blog/contact.html', ctx)


def register(request):
    ctg = Category.objects.all()
    forms = RegisterUp()
    if request.POST:
        forms = RegisterUp(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    ctx = {
        'ctg': ctg,
        'forms': forms
    }
    return render(request, 'blog/register.html', ctx)


def single(request, pk=None):
    ctg = Category.objects.all()
    sneakers = Sneakers.objects.all()
    random_pl = random.choices(sneakers,k=3)
    product_pk = Sneakers.objects.get(pk=pk) #Bu foydanauvchi tanlagan productni olish uchun shunaqa qilib shart beramiz.
    forms = ChoiceFrom()
    if request.POST:
        forms = ChoiceFrom(request.POST or None,
                           request.FILES or None)
        if forms.is_valid():
            root = forms.save()
            root = Buy.objects.get(pk=root.id)
            root.product = product_pk
            root.save()
            return redirect('home')
        else:
            print(forms.errors)
    ctx = {
        'ctg': ctg,
        'product_pk': product_pk,
        "forms": forms,
        'random_pl': random_pl,
        'sneakers': sneakers
    }
    return render(request, 'blog/single.html', ctx)
