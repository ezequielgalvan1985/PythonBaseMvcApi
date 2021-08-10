from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from rest_framework import status, mixins
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *








#TABLAS DEL SISTEMA



class UserCreate(generics.CreateAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
  permission_classes=()

  def post(self, request):
    print("ingreso a login")

    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)

    if user:
      return Response({"token":user.auth_token.key})
    else:
      return Response ({"error":"Wrong Credentials"}, status=400)



class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


#Tablas del NEGOCIOs
class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MarcaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer




class PedidoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


    @action(detail=False)
    def ultimopedido(self, request):
        print("ultimo pedido", request.data['dni'])
        if Pedido.objects.count() > 0:
            p = Pedido.objects.all().order_by('-id')[0]
            s = self.get_serializer(p, many=False)
            response = Response(s.data)
        else:
            response = Response({"detail":"No existe pedidos"}, status=status.HTTP_400_BAD_REQUEST)
        return response



class PedidodetalleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Pedidodetalle.objects.all()
    serializer_class = PedidodetalleSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class UnidadmedidaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Unidadmedida.objects.all()
    serializer_class = UnidadmedidaSerializer



class ParametroViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Parametro.objects.all()
    serializer_class = ParametroSerializer


class PromoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer

#Fin tabla de negocios



class HorarioViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer





#Ejemplo de ApiView Custom
@api_view(['GET'])
def CurrentUserProfileView(request):

    if request.method == 'GET':
        queryset = UserProfile.objects.filter(user=request.user)
        serializer_class = UserProfileSerializer(queryset,many=True)
        return Response(serializer_class.data)

