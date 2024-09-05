from django.test import TestCase
from myapp.models import Category

# Create your tests here.

#Inserción
t = Category()
t.name = 'Lacteos'
t.save()

"""
#Edición
t = Type.objects.get(id=1)
print(t.name)

#Consulta
query = Type.objects.all()
print(query)

#Like
obj = Type.objects.filter(name__contains='rlo').count()
print(obj)

"""
