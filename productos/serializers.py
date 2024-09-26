# productos/serializers.py

from django.contrib.auth.models import User  # Importar el modelo de usuario de Django
from rest_framework import serializers
from .models import Usuario, Roles, Pais

class UsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)  # Campo para el nombre de usuario
    password = serializers.CharField(write_only=True)  # Campo para la contraseña

    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'genero', 'correo', 'fk_rol', 'username', 'password']  # Incluimos username y password

    def create(self, validated_data):
        # Crear el usuario en la tabla auth_user
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        
        # Crear el usuario en la tabla Usuario vinculando el user_id
        usuario = Usuario.objects.create(
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            genero=validated_data.get('genero', None),  # Opcional
            correo=validated_data['correo'],
            fk_rol=validated_data.get('fk_rol', None),  # Opcional
            user=user  # Enlazar el user_id al modelo Usuario
        )

        return usuario

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['id_rol', 'descripcion']

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id', 'descripcion', 'moneda']  # Incluye los campos que quieres exponer en la API
