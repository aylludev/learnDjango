from django.http import JsonResponse
from django.shortcuts import render, reverse
from myapp.forms import CategoryForm
from myapp.models import Category
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

def category_list(request):
    data = {
        'title': 'Listado de Categorias',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        print(reverse_lazy('category_list'))
        return context
    

class CategoryCreateview(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    succes_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Creación de una Categoria'
        return context
