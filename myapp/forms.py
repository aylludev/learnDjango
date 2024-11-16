from django.forms import ModelForm
from myapp.models import Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
