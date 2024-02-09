from django.http import JsonResponse
from .models import Contraseña
from django.views.decorators.csrf import csrf_exempt
import json
import pdb

# Creo mis vistas / funciones, estas son las que harán las acciones




#Esta función listará todos mis usuarios y contraseñas
def password_list(request):
    
    # Vista para obtener todas las contraseñas y devolverlas en formato JSON.
    passwords = Contraseña.objects.all()    # Le asigno el valor de mostrarlo todo. 
    data = [{'usuario': password.usuario, 'contrasena': password.contrasena} for password in passwords] # Le asigno el valor del json 
    return JsonResponse({'passwords': data})


@csrf_exempt    # Utilizo el @crsf_exempt, para así poder usarlos mediante el POST
#Esta función añadirá un nuevo usuario.
def add_password(request):
 
    data = request.POST
        
    # Lo convierto a string, ya que me llega en b(bites) y no puedo operar así.
    my_json = json.loads(request.body.decode('utf8').replace("'", '"'))
    
    usuario = my_json['usuario']
    contrasena = my_json['contrasena']
    
    # Aqui filtro, ya que es un POST para así a ese usuario asignarle la función elegida
    Contraseña.objects.create(usuario=usuario, contrasena=contrasena)
    return JsonResponse({'Su contraseña se ha guardado con exito' : '.'})


@csrf_exempt    # Utilizo el @crsf_exempt, para así poder usarlos mediante el POST
#Esta función modificara la contraseña de un usuario ya existente.
def edit_password(request):
    
    data = request.POST
    # Lo convierto a string, ya que me llega en b(bites) y no puedo operar así.
    my_json = json.loads(request.body.decode('utf8').replace("'", '"'))

    usuario = my_json['usuario']
    contrasena = my_json['contrasena']

    # Aqui filtro, ya que es un POST para así a ese usuario asignarle la función elegida
    Contraseña.objects.filter(usuario=usuario).update(contrasena=contrasena)
    return JsonResponse ({'Buenas, esta es su nueva contraseña': contrasena})


@csrf_exempt    # Utilizo el @crsf_exempt, para así poder usarlos mediante el POST
#Esta función eliminará el usuario y la contraseña
def delete_password(request):
    
    data = request.POST
    
    # Lo convierto a string, ya que me llega en b(bites) y no puedo operar así.
    my_json = json.loads(request.body.decode('utf8').replace("'", '"'))

    usuario = my_json['usuario']
    contrasena = my_json['contrasena']
    
    # Aqui filtro, ya que es un POST para así a ese usuario asignarle la función elegida
    Contraseña.objects.filter(usuario=usuario, contrasena=contrasena).delete()
    return JsonResponse({'Su contraseña se ha eliminado con exito' : '.'})
