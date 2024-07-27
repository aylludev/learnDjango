from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Categoria',unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre',unique=True)
    cate = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.0,max_digits=9, decimal_places=2)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Tipo')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'tipo'
        ordering = ['id']

class Employee(models.Model):
    id = models.CharField(primary_key=True, max_length=10, unique=True, verbose_name='Cedula')
    names = models.CharField(max_length=150, verbose_name='Nombres')
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    date_joined = models.DateField(default=datetime.now, verbose_name='Nombre de registro')
    date_created= models.DateTimeField(auto_now=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar')
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering= ['id']