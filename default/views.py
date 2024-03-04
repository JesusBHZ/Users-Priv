from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from .models import Usuarios, Tablas, Productos, Privilegios, Usuarios_Privilegios_Tablas
from django.shortcuts import get_object_or_404, render, redirect
from django.apps import apps
import json
import ast

def index(request):
    listaUsuarios = list(Usuarios.objects.values())
    listaPrivilegios = list(Privilegios.objects.values())
    listaTablas = list(Tablas.objects.values())

    return render(request, 'index.html', {
        'listaPrivilegios': listaPrivilegios,
        'listaTablas': listaTablas,
        'listaUsuarios':listaUsuarios
    })

def usuarios(request):
    usuarios = list(Usuarios.objects.values())
    print(usuarios)
    return render(request, 'usuarios/usuarios.html', {
        'usuarios': usuarios
    })

def insertUsuario(request):
    try:
        name = request.POST.get('input-name', '')
        password = request.POST.get('input-password', '')
        rol = request.POST.get('input-rol', '')
        status = request.POST.get('input-status', '')
        print(status)
        user = Usuarios(nombre=name, password=password, rol=rol, status=status)
        print(user)
        user.save()

        return redirect('usuarios')

    except Exception as e:
        return redirect('usuarios')

def deleteUsuario(request):
    try:
        id = request.POST.get('input-id', '')
        user = Usuarios.objects.get(pk=int(id))
        user.delete()
        return redirect('usuarios')

    except Exception as e:
        return redirect('usuarios')

def updateUsuario(request):
    try:
        id = request.POST.get('input-id', '')
        name = request.POST.get('input-name', '')
        password = request.POST.get('input-password', '')
        rol = request.POST.get('input-rol', '')
        status = request.POST.get('input-status', '')
        
        user = Usuarios.objects.get(pk=int(id))
        user.nombre = name
        user.password = password
        user.rol = rol
        user.status = status
        user.save()

        return redirect('usuarios')

    except Exception as e:
        return redirect('usuarios')


def queryUsuario(request):
    try:
        print("holi")
        id = request.POST.get('input-id', '')
        user = Usuarios.objects.get(pk=int(id))
        usuario = list(user)
        return render(request, 'usuarios/usuarios.html', {
            'usuario': usuario
        })

    except Exception as e:
        return redirect('usuarios')


def tablas(request):
    tablas = list(Tablas.objects.values())
    
    return render(request, 'tablas/tablas.html', {
        'tablas': tablas
    })

def insertTabla(request):
    try:
        name = request.POST.get('input-name', '')
        descripcion = request.POST.get('input-descripcion', '')
        table = Tablas(name_tabla=name, description=descripcion)
        table.save()

        return redirect('tablas')

    except Exception as e:
        return redirect('tablas')


def deleteTabla(request):
    try:
        id = request.POST.get('input-id', '')
        table = Tablas.objects.get(pk=int(id))
        table.delete()
        return redirect('tablas')

    except Exception as e:
        return redirect('tablas')

def updateTabla(request):
    try:
        id = request.POST.get('input-id', '')
        table = Tablas.objects.get(pk=int(id))
        print("table")
        table.name_tabla = request.POST.get('input-name', '')
        table.description = request.POST.get('input-descripcion', '')
        
        table.save()

        return redirect('tablas')

    except Exception as e:
        return redirect('tablas')

def queryTabla(request):
    try:
        id = request.POST.get('input-id', '')
        table = Tablas.objects.get(pk=int(id))
        tabla = list(table)
        return render(request, 'tablas/tablas.html', {
            'tabla': tabla
        })

    except Exception as e:
        return redirect('usuarios')


def privilegios(request):
    privilegios = list(Privilegios.objects.values())
    
    return render(request, 'privilegios/privilegios.html', {
        'privilegios': privilegios
    })


def insertPrivilegios(request):
    try:
        name = request.POST.get('input-privilegios', '')
        descripcion = request.POST.get('input-descripcion', '')
        privilegios = Privilegios(name_privilegio=name, description=descripcion)
        privilegios.save()

        return redirect('privilegios')

    except Exception as e:
        return redirect('privilegios')


def deletePrivilegios(request):
    try:
        id = request.POST.get('input-id', '')
        privilegio = Privilegios.objects.get(pk=int(id))
        privilegio.delete()
        return redirect('privilegios')

    except Exception as e:
        return redirect('privilegios')

def updatePrivilegios(request):
    try:
        id = request.POST.get('input-id', '')
        privilegio = Privilegios.objects.get(pk=int(id))
        privilegio.name_privilegio = request.POST.get('input-privilegios', '')
        privilegio.description = request.POST.get('input-descripcion', '')
        
        privilegio.save()

        return redirect('privilegios')

    except Exception as e:
        return redirect('privilegios')

def queryPrivilegios(request):
    try:
        id = request.POST.get('input-id', '')
        privilegio = Privilegios.objects.get(pk=int(id))
        privilegio = list(privilegio)
        return render(request, 'privilegios/privilegios.html', {
            'privilegio': privilegio
        })

    except Exception as e:
        return redirect('usuarios')


def productos(request):
    productos = list(Productos.objects.values())
    
    return render(request, 'productos/productos.html', {
        'productos': productos
    })


def insertProductos(request):
    try:
        name = request.POST.get('input-productos', '')
        descripcion = request.POST.get('input-descripcion', '')
        precio = request.POST.get('input-precio', '')
        productos = Productos(name_producto=name, description=descripcion, precio=precio)
        productos.save()

        return redirect('productos')

    except Exception as e:
        return redirect('productos')

def deleteProductos(request):
    try:
        id = request.POST.get('input-id', '')
        productos = Productos.objects.get(pk=int(id))
        productos.delete()
        return redirect('productos')

    except Exception as e:
        return redirect('productos')



def updateProductos(request):
    try:
        id = request.POST.get('input-id', '')
        productos = Productos.objects.get(pk=int(id))
        productos.name_producto = request.POST.get('input-productos', '')
        productos.description = request.POST.get('input-descripcion', '')
        productos.precio = request.POST.get('input-precio', '')
        
        productos.save()

        return redirect('productos')

    except Exception as e:
        return redirect('productos')

def queryProductos(request):
    try:
        id = request.POST.get('input-id', '')
        productos = Productos.objects.get(pk=int(id))
        productos = list(productos)
        return render(request, 'productos/productos.html', {
            'productos': productos
        })

    except Exception as e:
        return redirect('productos')


def assignPrivilegios(request):
    usuario = request.POST.get('select-usuarios', '')
    privilegio = request.POST.get('select-privilegios', '')
    tabla = request.POST.get('select-tabla', '')

    id_usuario = Usuarios.objects.get(pk=int(usuario))
    id_privilegio = Privilegios.objects.get(pk=int(privilegio))
    id_tabla = Tablas.objects.get(pk=int(tabla))

    usuarios_privilegios_tabla = Usuarios_Privilegios_Tablas(id_usuario=id_usuario, id_privilegio=id_privilegio, id_tabla=id_tabla)
    usuarios_privilegios_tabla.save()

    return redirect('index')


def consultasUsersAndPrivilegios(request):
    try:
        usuario = request.POST.get('select-usuarios', '')
        password = request.POST.get('input-password', '')
        query = request.POST.get('input-query', '')

        user = Usuarios.objects.get(pk=int(usuario))

        if user.password == password:
            query_array = query.split()
            
            if query_array[0].upper() == 'SELECT':
                result = SELECT(query_array, user)
            elif query_array[0].upper() == 'UPDATE':
                result = UPDATE(query_array, user)
            elif query_array[0].upper() == 'INSERT':
                result = INSERT(query_array, user, query)
            elif query_array[0].upper() == 'DELETE':
                result = DELETE(query_array, user)
            else:
                return HttpResponse({"status": 400, "result": [{

                    "estatus":"Sintax Error"
                }]}, status=400)
        else:
            return HttpResponse({"status": 406, "result": [{

                "estatus":"Usuario y contraseña incorrecta"
            }]}, status=406)  
        
        if result == 400:
            result =  {"status": "No tienes permisos"} 

        return JsonResponse({"status": 202, "result": result}, status=202)
    except Usuarios.DoesNotExist:
        return HttpResponse({"status": 404, "result": [{

            "estatus":"Ocurrio un error"
        }]}, status=404)
    except Exception as e:
        print(e)
        return HttpResponse(
            {"status": 400, "result": [{"estatus": "No tienes permisos", "error": str(e)}]},
            status=400
        )

def SELECT(query, user):
    result = []  
    newTabla = query[-1].split(";")
    tabla = newTabla[0]
    objectTable = Tablas.objects.get(name_tabla=tabla.title())
    objectPrivilegio = Privilegios.objects.get(name_privilegio="SELECT")
    consultaPrivilegios = Usuarios_Privilegios_Tablas.objects.get(id_usuario=user, id_privilegio=objectPrivilegio, id_tabla=objectTable)
    
    if consultaPrivilegios:
        print("si hay cpn")
        app_label = 'default'
        print(tabla.title())
        tbl = tabla.title()
        ModeloDinamico = apps.get_model(app_label=app_label, model_name=tbl)
        print(ModeloDinamico)
        consulta = ModeloDinamico.objects.all()
        
        for objeto in consulta:
            nombre_producto = objeto.name_producto
            precio = objeto.precio
            description = objeto.description
            resultado = {'Nombre': nombre_producto, 'Precio': precio, 'Descripcion': description}
            result.append(resultado)
        print(result)
        #json_result = json.dumps(result, indent=2)
        print("triste")
        #print(json_result)
        return result
    else:
        return 400


def UPDATE(query, user):
    result = {
            "status": "Cambio exitoso",
        }
        
    
    newTabla = query[1].title()
    objectTable = Tablas.objects.get(name_tabla=newTabla)
    objectPrivilegio = Privilegios.objects.get(name_privilegio="UPDATE")

    try:
        consultaPrivilegios = Usuarios_Privilegios_Tablas.objects.get(id_usuario=user, id_privilegio=objectPrivilegio, id_tabla=objectTable)

        change = query[3].split("=")
        changeColumn = change[0]
        changeValue = change[1]

        condition = query[-1].split("=")
        conditionColumn = condition[0]
        
        
        co = condition[1].strip()  
        if str(co).endswith(";"):
            conditionValue = co[:-1]  
        else:
            conditionValue = co
        
        app_label = 'default'
        ModeloDinamico = apps.get_model(app_label=app_label, model_name=newTabla)
        print(ModeloDinamico)


        update = ModeloDinamico.objects.get(pk=conditionValue)
        valor_del_atributo = getattr(update, changeColumn, None)
        update.__setattr__(changeColumn, changeValue)
        update.save()

        json_result = json.dumps(result, indent=2)
        return json_result
    
    except Usuarios_Privilegios_Tablas.DoesNotExist:
        return 400



def DELETE(query, user):
    try:
        result = {
                "status": "Eliminacion exitosa",
            }
        
        print("DELETE")
        # DELETE FROM productos WHERE id_producto=1;
        
        newTabla = query[2].title()
        print(newTabla)
        objectTable = Tablas.objects.get(name_tabla=newTabla)
        objectPrivilegio = Privilegios.objects.get(name_privilegio="DELETE")

        consultaPrivilegios = Usuarios_Privilegios_Tablas.objects.get(id_usuario=user, id_privilegio=objectPrivilegio, id_tabla=objectTable)

        condition = query[-1].split("=")
        conditionColumn = condition[0]
        
        
        co = condition[1].strip()  
        if str(co).endswith(";"):
            conditionValue = co[:-1]  
        else:
            conditionValue = co

        app_label = 'default'
        ModeloDinamico = apps.get_model(app_label=app_label, model_name=newTabla)
        delet = ModeloDinamico.objects.get(pk=conditionValue)

        delet.delete()

        json_result = json.dumps(result, indent=2)
        return json_result
    except Usuarios_Privilegios_Tablas.DoesNotExist:
        return 400



def INSERT(query, user, consulta):
    # INSERT INTO productos (producto,descripcion,precio) VALUES(’producto 1’,’Producto de prueba’,100.00);
    try:
        result = {
                "status": "Registro exitoso"}        
        print("INSERT")

        newTabla = query[2].title()
        objectTable = Tablas.objects.get(name_tabla=newTabla)
        objectPrivilegio = Privilegios.objects.get(name_privilegio="INSERT")

        consultaPrivilegios = Usuarios_Privilegios_Tablas.objects.get(id_usuario=user, id_privilegio=objectPrivilegio, id_tabla=objectTable)

        campos = query[3]
        cadena_sin_parentesis = campos.replace("(", "").replace(")", "")
        camposTabla = cadena_sin_parentesis.split(",")
        
        
        inicio_valores = consulta.find("VALUES") + len("VALUES")
        fin_valores = consulta.find(";")

        # Extraer la parte de los valores
        valores = consulta[inicio_valores:fin_valores].strip()

        valores_sin_parentesis = valores.replace("(", "").replace(")", "")
        hola_sin_comillas = valores_sin_parentesis.replace("’", "")

        valuesInsert = hola_sin_comillas.split(",")
       
        datos_a_insertar = dict(zip(camposTabla, valuesInsert))
       
        nuevo_objeto = Productos(name_producto=valuesInsert[0], description=valuesInsert[1], precio=valuesInsert[2])
        nuevo_objeto.save()
        
        json_result = json.dumps(result, indent=2)
        return json_result

    except Usuarios_Privilegios_Tablas.DoesNotExist:
        return 400
