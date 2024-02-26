"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from default import views
import default

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', default.views.index, name="index"),
    path('usuarios', default.views.usuarios, name="usuarios"),
    path('insertusuario', default.views.insertUsuario, name="insertUsuario"),
    path('deleteUsuario', default.views.deleteUsuario, name="deleteUsuario"),
    path('updateUsuario', default.views.updateUsuario, name="updateUsuario"),
    path('queryUsuario', default.views.queryUsuario, name="queryUsuario"),

    path('tablas', default.views.tablas, name="tablas"),
    path('insertTabla', default.views.insertTabla, name="insertTabla"),
    path('deleteTabla', default.views.deleteTabla, name="deleteTabla"),
    path('updateTabla', default.views.updateTabla, name="updateTabla"),
    path('queryTabla', default.views.queryTabla, name="queryTabla"),

    path('privilegios', default.views.privilegios, name="privilegios"),
    path('insertPrivilegios', default.views.insertPrivilegios, name="insertPrivilegios"),
    path('queryPrivilegios', default.views.queryPrivilegios, name="queryPrivilegios"),
    path('deletePrivilegios', default.views.deletePrivilegios, name="deletePrivilegios"),
    path('updatePrivilegios', default.views.updatePrivilegios, name="updatePrivilegios"),

    path('productos', default.views.productos, name="productos"),
    path('insertProductos', default.views.insertProductos, name="insertProductos"),
    path('deleteProductos', default.views.deleteProductos, name="deleteProductos"),
    path('updateProductos', default.views.updateProductos, name="updateProductos"),
    path('queryProductos', default.views.queryProductos, name="queryProductos"),


    path('assignPrivilegios', default.views.assignPrivilegios, name="assignPrivilegios"),
    path('consultasUsersAndPrivilegios', default.views.consultasUsersAndPrivilegios, name="consultasUsersAndPrivilegios"),
]
