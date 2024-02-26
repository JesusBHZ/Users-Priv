from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.html import format_html
from datetime import date

class Usuarios(models.Model):
    nombre = models.CharField(max_length=150, null=True)
    password = models.CharField(max_length=10, null=True)
    rol = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=50, null=True)
    fecha_actualizacion = models.DateField(default=date.today, null=True)

    class Meta:
        db_table = 'usuarios'

class Privilegios(models.Model):
    name_privilegio = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=150, null=True)

    class Meta:
        db_table = 'privilegios'

class Usuarios_Privilegios_Tablas(models.Model):
    id_usuario = models.ForeignKey('Usuarios', null=True, on_delete=models.SET_NULL)
    id_privilegio = models.ForeignKey('Privilegios', null=True, on_delete=models.SET_NULL)
    id_tabla = models.ForeignKey('Tablas', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'usuarios_privilegios_tablas'

class Tablas(models.Model):
    name_tabla = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=150, null=True)

    class Meta:
        db_table = 'tablas'


class Productos(models.Model):
    name_producto = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=150, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'productos'