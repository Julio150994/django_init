from django.shortcuts import redirect, render
from principal.models import Persona
from .forms import PersonaForm

# Create your views here.

def inicio(request): #request: petición del navegador#
    personas = Persona.objects.all() #R: listar contactos#
    print(personas)
    contexto = {
        'personas':personas
    }
    return render(request,"principal/index.html",contexto)

def crearPersona(request):
    if request.method == 'GET': #C: crear contacto#
        form = PersonaForm()
        contexto = {
            'form':form
        }
    else: #Para capturar cada dato y enviar a través de los input a la BBDD#
        form = PersonaForm(request.POST)
        contexto = {
            'form':form
        }
        
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'principal/crear_persona.html',contexto)

def editarPersona(request, id): #buscamos contacto por id además#
    persona = Persona.objects.get(id = id) #id es lo que ponemos en el urls.py como <int:id>/#
    #Imprimimos los datos del contacto en los inputs del formulario mediante id#
    if request.method == 'GET':
        #Creamos una instancia para visualizar datos de formulario de persona#
        form = PersonaForm(instance = persona)
        contexto = {
            'form':form
        }
    else: #Realizamos la acción de editar el contacto (de manera similar que añadir contacto)#
        form = PersonaForm(request.POST, instance = persona)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    #return render(request,'principal/editar_persona.html',contexto) para hacer el editar en otra plantilla (opción 1)#
    return render(request,'principal/crear_persona.html',contexto) #para hacer el editar en la misma plantilla (opción 2)#

def eliminarPersona(request, id):
    # Eliminamos contacto de la manera más simple, es decir, sin mensaje de confirmación#
    persona = Persona.objects.get(id = id)
    persona.delete() #para realizar la acción de eliminar#
    return redirect('index')