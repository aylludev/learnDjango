
from django.urls import path, include
from myapp.views.category.views import category_list

urlpatterns = [
    path('category/list', category_list, name= 'category_list' )
]
