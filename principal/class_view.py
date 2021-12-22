from django.shortcuts import redirect, render
from django.views.generic import CreateView,DeleteView,ListView,UpdateView #View
from django.urls import reverse_lazy
from .forms import PersonaForm
from .models import Persona

"""
class View():
    dispatch: verificar el método de la solicitud http
    http_not_allowed

    def get_queryset(self):
        return self.model.objects.all()

    def get_templates_names():
        return self.template_name

    def get(self,request, *args,**kwargs):
        return render(request, self.get_template_names(), self.get_queryset())


class ListView(View):
    model = Persona
    template_name = 'index.html'

    def dispatch()

    def get_context_data(self):
        context = {}
        context['queryset'] = self.get_queryset()
        return context

    def get_queryset(self):
        return self.model.objects.all()

    def get_templates_names():
        return self.template_name

    def get(self,request, *args,**kwargs):
        return render(request, self.get_template_names(), self.get_queryset(), self.get_content_data())
"""

class PersonaList(ListView):
    model = Persona
    template_name = 'principal/index.html'

    """def get_queryset(self):
        return self.model.objects.all()[:2] #mostramos solamente los dos primeros usuarios#"""

#Aquí es lo mismo añadir que editar, para llamar al mismo ó a un formulario de otra vista#
class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'principal/crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'principal/crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'principal/verificacion.html'
    success_url = reverse_lazy('index')