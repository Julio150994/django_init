from django.contrib import admin
from django.urls import path
from principal.views import inicio, crearPersona, editarPersona, eliminarPersona
from principal.class_view import PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete

urlpatterns = [
    #path('',inicio, name = "index"),<----- el inicio hecho en views.py
    path('', PersonaList.as_view(), name="index"), #<------- el inicio hecho en class_view.py#
    #path('crear_persona/',crearPersona, name="crear_persona"),
    path('crear_persona/', PersonaCreate.as_view(), name="crear_persona"),
    #path('editar_persona/<int:id>/',editarPersona, name="editar_persona") id es para el views.py,
    path('editar_persona/<int:pk>/', PersonaUpdate.as_view(), name="editar_persona"), #el pk es para el class_view.py# 
    #path('eliminar_persona/<int:id>/', eliminarPersona, name="eliminar_persona"), hacemos lo mismo para eliminar, en cuanto a recoger el id
    path('eliminar_persona/<int:pk>/', PersonaDelete.as_view(), name="eliminar_persona"),
]