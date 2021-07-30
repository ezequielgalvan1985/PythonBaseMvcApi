from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Marca(models.Model):
    nombre      = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre      = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=200,blank=True, null=True)
    def __str__(self):
        return self.nombre

class Unidadmedida(models.Model):
    nombre      = models.CharField(max_length=50,  blank=False, null=False)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre         = models.CharField(max_length=50)
    descripcion    = models.CharField(max_length=200, blank=True, null=True)
    preciounitario = models.DecimalField(default=0, decimal_places=3, max_digits=10, verbose_name='Precio Unitario')
    marca          = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True)
    categoria      = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    codigoexterno  = models.CharField(max_length=50, blank=True, verbose_name='Codigo Externo')
    stock          = models.IntegerField(default=0)
    imagen         = models.CharField(max_length=50, blank=True, null=False)
    enabled        = models.BooleanField(default=True, verbose_name='¿Producto En Venta?')
    ispromo        = models.BooleanField(default=False, verbose_name='¿En Promocion?')
    preciopromo    = models.DecimalField(default=0, decimal_places=3, max_digits=10, blank=True, null=True, verbose_name='Precio Promo')
    unidadmedida   = models.ForeignKey(Unidadmedida, on_delete=models.CASCADE, null=True)
    isfraccionado  = models.BooleanField(default=False, verbose_name='¿Es Fraccionado?')

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    nombre      = models.CharField(max_length=50,  blank=False, null=False)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    fecha      = models.DateTimeField('Fecha Creacion', auto_now=True)
    estado     = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1, blank=True, null=True)
    android_id = models.IntegerField(default=0)
    subtotal   = models.DecimalField(default=0, decimal_places=3, max_digits=10, blank=True, null=True)
    monto      = models.DecimalField(default=0, decimal_places=3, max_digits=10, blank=True, null=True)
    montoabona = models.DecimalField(default=0, decimal_places=3, max_digits=10, blank=True, null=True)
    cliente    = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    localidad  = models.CharField(max_length=50)
    calle      = models.CharField(max_length=50)
    piso       = models.CharField(max_length=10, blank=True, null=True)
    nro        = models.CharField(max_length=10)
    telefono   = models.CharField(max_length=25)
    contacto   = models.CharField(max_length=50)
    montodescuento    = models.DecimalField('Descuento $',default=0, decimal_places=3, max_digits=10, blank=True, null=True)
    cantidaddescuento = models.DecimalField('Descuento U.',default=0, decimal_places=3, max_digits=10, blank=True, null=True)
    enviodomicilio    = models.BooleanField(default=False, verbose_name='¿Envio a Domicilio?')
    visto             = models.BooleanField(default=False)
    impreso           = models.BooleanField(default=False)
    tiempodemora      = models.CharField(max_length=10, default='00:45', verbose_name='Tiempo Demora',  blank=True, null=True)
    horarecepcion     = models.DateTimeField('Hora Recepcion', auto_now=False,blank=True, null=True)
    horaentregado     = models.DateTimeField('Hora Entregado', auto_now=False,blank=True, null=True)
    def __str__(self):
        return str(self.id)

class Pedidodetalle(models.Model):
    cantidad = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    pedido   = models.ForeignKey(Pedido, on_delete=models.CASCADE,related_name='items')
    producto = models.ForeignKey(Producto,  on_delete=models.CASCADE)


class Parametro(models.Model):
    nombre       = models.CharField(max_length=50)
    descripcion  = models.CharField(max_length=100)
    valortexto   = models.CharField(max_length=100, blank=True, null=True)
    valorinteger = models.IntegerField( default=0,blank=True, null=True)
    valordecimal = models.DecimalField(default=0, decimal_places=3, max_digits=10, blank=True, null=True)
    valorfecha   = models.DateTimeField('Fecha',blank=True, null=True)

    def __str__(self):
        return self.nombre



class Promo (models.Model):
    nombre           = models.CharField(max_length=50)
    descripcion      = models.CharField(max_length=100)
    enabled          = models.CharField(max_length=100)
    producto         = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad         = models.IntegerField()
    preciopromo      = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    importedescuento = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    precioanterior   = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    fechadesde       = models.DateTimeField('Fecha Desde')
    fechadesde       = models.DateTimeField('Fecha Hasta')

    def __str__(self):
        return self.nombre



class Dispenser(models.Model):
    nombre      = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    serie = models.CharField(max_length=200, blank=True, null=True)
    orden = models.IntegerField()

    def __str__(self):
        return self.nombre


