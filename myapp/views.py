from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def myfirstview(request):
    data = {
        'name' : 'William'
    }
    return render(request, 'index.html', data)