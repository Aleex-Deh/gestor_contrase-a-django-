from django.http import JsonResponse
from .models import Contraseña
from django.views.decorators.csrf import csrf_exempt
import json
import pdb


# Create your views here.


def password_list(request):
    # Vista para obtener todas las contraseñas y devolverlas en formato JSON.
    passwords = Contraseña.objects.all()
    data = [{'usuario': password.usuario, 'contrasena': password.contrasena} for password in passwords]
    return JsonResponse({'passwords': data})


@csrf_exempt
def add_password(request):
 
    # Vista para agregar una nueva contraseña a través de una solicitud POST y devolver una respuesta JSON.
    print("********************* ASDFASDF ")
    data = request.POST
    print("********************* ASDFASDF ")
    #usuario = data.get('usuario')
    #contrasena = data.get('contrasena')
    
    # Lo convierto a string
    my_json = json.loads(request.body.decode('utf8').replace("'", '"'))
    # Con lo definido para convertir a string se lo añado a mis variables, yaque antes eran butes, y ahora seeran string, con bytes no se puede trabajar 
    usuario = my_json['usuario']
    contrasena = my_json['contrasena']
    Contraseña.objects.create(usuario=usuario, contrasena=contrasena)
    return JsonResponse({'status': 'success'})


@csrf_exempt
def edit_password(request):
    pdb.set_trace()
    # Vista para editar una contraseña existente mediante una solicitud POST y devolver una respuesta JSON.
    data = request.POST
    my_json = json.loads(request.body.decode('utf8').replace("'", '"'))

    usuario = my_json['usuario']
    contrasena = my_json['contrasena']

    
    Contraseña.objects.filter(usuario="macia").update(contrasena=contrasena)

    #valor =  Contraseña.objects.get(usuario="macia")

    return JsonResponse({'status': contrasena})


@csrf_exempt
def delete_password(request, pk):
    # Vista para eliminar una contraseña existente mediante una solicitud POST y devolver una respuesta JSON.
    Contraseña.objects.filter(pk=pk).delete()
    return JsonResponse({'status': 'success'})
