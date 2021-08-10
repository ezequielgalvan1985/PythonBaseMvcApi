from django.contrib.auth.models import User, Group
#from .models import Categoria, Marca, Dispenser, Producto, Pedido, Pedidodetalle, Parametro, Promo, Estado, Unidadmedida
from .models import *
from rest_framework import serializers
from rest_framework.authtoken.models import Token






class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email','password','groups')
        extra_kwargs={'password':{'write_only':True}}
        
    def create(self, validated_data):
        user = User(email = validated_data['email'], username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
      
    



class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','nombre','descripcion']



class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre', 'descripcion']


class UnidadmedidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unidadmedida
        fields = ['id','nombre','descripcion','abreviatura']


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    marca        = MarcaSerializer(read_only=True)
    categoria    = CategoriaSerializer(read_only=True)
    unidadmedida = UnidadmedidaSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion','precio', 'marca','categoria'
                   ,'codigoexterno', 'stock', 'imagen', 'enabled',
                  'ispromo', 'preciopromo','unidadmedida', 'isfraccionado']



class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user','id', 'nombre',
                  'apellido','calle','nro','piso', 'contacto',
                  'telefono']



class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ['id','nombre','descripcion']


class PedidodetalleSerializer(serializers.HyperlinkedModelSerializer):
    producto    = ProductoSerializer(many=False, read_only=True)

    class Meta:
        model = Pedidodetalle
        fields = ['id','cantidad', 'producto']




class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    items     = PedidodetalleSerializer(many=True)
    estado    = EstadoSerializer(many=False, read_only=True)
    cliente   = UserSerializer(many=False, read_only=True)

    def create(self, validated_data):
        print(validated_data)

        tracks_data = validated_data.pop('items')
        print(tracks_data)

        pedido = Pedido.objects.create(**validated_data)
        for track_data in tracks_data:
            Pedidodetalle.objects.create(pedido=pedido, **track_data)
        return pedido


    class Meta:
        model = Pedido
        fields = ['id', 'android_id','estado','cliente',
                  'subtotal','monto','id','fecha',
                  'localidad','calle','nro','telefono','contacto','items'
                  ]











#tutorial

class PromoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'



class ParametroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parametro
        fields = ['id','nombre', 'descripcion','valor_fecha',
                  'valor_integer','valor_decimal', 'valor_texto']



class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horario
        fields = ['id','dia','apertura','cierre', 'observaciones']




