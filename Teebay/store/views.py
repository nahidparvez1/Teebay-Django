from email import message
from itertools import product
from multiprocessing import context
from pyexpat.errors import messages
from unicodedata import category
from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def home(request):
    return render(request, "store/index.html")

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request, "store/collections.html", context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category':category}
        return render(request, "store/products/index.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')