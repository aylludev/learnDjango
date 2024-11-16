from django.db import models
from django.forms import model_to_dict

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre',unique=True)

    def __str__(self):
        return self.name
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']

class Product(models.Model):
    id_pro = models.CharField(primary_key=True, max_length=15, unique=True, verbose_name='id_pro')
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
        ordering = ['id_pro']

class Client(models.Model):
    id_cli = models.CharField(primary_key=True, max_length=15, unique=True, verbose_name='Cedula')
    names = models.CharField(max_length=150, verbose_name='Nombres')
    lastnames = models.CharField(max_length=150, verbose_name='Apellidos')
    date_nac= models.DateTimeField(auto_now=True)
    direction = models.CharField(max_length=150, verbose_name='Direccion')
    gendre = models.CharField(max_length=150, verbose_name='Genero')


    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'clientes'
        ordering= ['id_cli']

class Sale(models.Model):
    id_sale = models.CharField(primary_key=True, max_length=150, unique=True, verbose_name='Id_venta')
    id_cli = models.ForeignKey(Client, max_length=15, on_delete=models.CASCADE)
    date_sale= models.DateTimeField(auto_now=True)
    subtotal = models.FloatField()
    iva = models.FloatField()
    total = models.FloatField()
    

    def __str__(self):
        return self.id_sale
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'ventas'
        ordering= ['id_sale']

class DetSale(models.Model):
    id_det = models.CharField(primary_key=True, max_length=15, unique=True, verbose_name='Id_venta')
    id_sale = models.ForeignKey(Sale, max_length=15, on_delete=models.CASCADE)
    id_pro = models.CharField(Product, max_length=15)
    quanty = models.FloatField()
    price = models.FloatField()
    subtotal = models.FloatField()    

    def __str__(self):
        return self.id_sale
    
    class Meta:
        verbose_name = 'DetVenta'
        verbose_name_plural = 'DetVentas'
        db_table = 'detventas'
        ordering= ['id_det']
