from django.db import models
from django.contrib.auth.models import User

# Modelo Pais - Mapeado a la tabla ya existente en la base de datos
class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    moneda = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'pais'  # Nombre exacto de la tabla en la BD
        managed = False
# Modelo Imagen - Mapeado a la tabla ya existente en la base de datos
class Imagen(models.Model):
    # Definición de la tabla imagen si la usas en la FK
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    moneda = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'imagen'  # Nombre exacto de la tabla en la BD
        managed = False
#Roles
class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)

    class Meta:
        db_table = 'roles'  # Asegúrate de usar el nombre exacto de la tabla en la BD
        managed = False  # Django no creará ni gestionará esta tabla 

# Modelo Usuario - Mapeado a la tabla 'usuario' ya existente
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    genero = models.CharField(max_length=50, blank=True, null=True)
    correo = models.EmailField(unique=True, max_length=255)  # Asegúrate de que el tamaño coincida con la tabla
    fk_rol = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, blank=True, db_column='fk_rol')  # Opcional
    fk_imagen = models.ForeignKey(Imagen, on_delete=models.SET_NULL, null=True, blank=True, db_column='fk_imagen')  # Opcional
    fk_pais = models.ForeignKey(Pais, on_delete=models.PROTECT, db_column='fk_pais')  # Obligatorio
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Esto generará automáticamente 'user_id'

    class Meta:
        db_table = 'usuario'  # Nombre exacto de la tabla en la BD


 
    
