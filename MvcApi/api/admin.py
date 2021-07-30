from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categoria, Marca, Producto, Dispenser, Pedido, Unidadmedida, Pedidodetalle, \
    Parametro, Estado


class AlbumAdmin(admin.ModelAdmin):
    fields = ['album_name', 'artist']


class TrackAdmin(admin.ModelAdmin):
    fields = ['producto','cantidad']

class CategoriaAdmin(admin.ModelAdmin):
    fields = ['nombre', 'descripcion']
    list_display = ('nombre', 'descripcion')

class MarcaAdmin(admin.ModelAdmin):
    fields = ['nombre', 'descripcion']
    list_display = ('nombre', 'descripcion')

class UnidadmedidaAdmin(admin.ModelAdmin):
    fields = ['nombre', 'descripcion']
    list_display = ('nombre', 'descripcion')

class ProductoAdmin(admin.ModelAdmin):
    field = (('nombre', 'descripcion'),'preciounitario')
    list_display = ('nombre', 'descripcion')

class PedidodetalleInline(admin.TabularInline):
    model = Pedidodetalle
    fields = ['cantidad','pedido', 'producto']


class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha']
    fieldsets = (
        ('Estado del Pedido', {
            'classes': ('collapse',),
            'fields': ('fecha', 'estado', 'cliente'),
        }),
        ('Datos de Contacto', {
            'classes': ('collapse',),
            'fields': ('contacto', 'localidad', 'calle', 'nro', 'piso', 'telefono'),
        }),
        ('Totales', {
            'classes': ('collapse',),
            'fields': ('subtotal', 'monto', 'montodescuento', 'cantidaddescuento', 'montoabona'),
        }),
        ('Tiempos del Pedido', {
            'classes': ('collapse',),
            'fields': ( 'impreso', 'tiempodemora', 'horarecepcion', 'horaentregado'),
        }),

    )
    inlines = [
        PedidodetalleInline,
    ]
    list_display = ('id', 'fecha','cliente','subtotal','montodescuento','monto')


class EstadoAdmin(admin.ModelAdmin):
    #model = Estado
    fields = ['nombre', 'descripcion']

class ParametroAdmin(admin.ModelAdmin):
    fields = ['nombre', 'descripcion','valortexto','valorinteger' ,'valordecimal', 'valorfecha' ]

class DispenserAdmin(admin.ModelAdmin):
    fields = ['nombre', 'descripcion','serie', 'orden']

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Unidadmedida, UnidadmedidaAdmin)

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Parametro, ParametroAdmin)
admin.site.register(Dispenser, DispenserAdmin)
