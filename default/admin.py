from django.contrib import admin
from .models import Usuarios, Privilegios, Tablas, Productos, Usuarios_Privilegios_Tablas

admin.site.register(Usuarios)
admin.site.register(Privilegios)
admin.site.register(Tablas)
admin.site.register(Productos)
admin.site.register(Usuarios_Privilegios_Tablas)
