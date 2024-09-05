from django.shortcuts import render
from myapp.models import Product, Category
from django.http import HttpResponse, JsonResponse


# Create your views here.
def myfirstview(request):
    data = {
        'name' : 'William',
        'categories' : Category.objects.all()
    }
    return render(request, 'index.html', data)

def mysecondview(request):
    data = {
        'name' : 'William',
        'products' : Product.objects.all()
    }
    return render(request, 'second.html', data)

def invoiceview(request):
    data = {
        'name' : 'William',
        'products' : Product.objects.all()
    }
    return render(request, 'invoice.html', data)