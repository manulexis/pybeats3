# views.py
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Usuario, Roles,Pais  
from .serializers import UsuarioSerializer, RolesSerializer,PaisSerializer  

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación

    def create(self, request, *args, **kwargs):
        # Aquí puedes manejar la creación del usuario, y cualquier validación extra si es necesario
        return super().create(request, *args, **kwargs)

class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    permission_classes = [AllowAny] 

# ViewSet para Países
class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()  # Obtenemos todos los países
    serializer_class = PaisSerializer  # Serializador de Países
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación



