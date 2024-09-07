
from django.urls import path, include
from myapp.views.category.views import *

urlpatterns = [
    path('category/list', CategoryListView.as_view(), name= 'category_list' )
]
