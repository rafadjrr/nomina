from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from apps.empleado.models import Empleado
from apps.departamento.models import *
from .forms import *
# Create your views here.

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('aqui estoy en el formulario')
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            nick = form.cleaned_data['shortname']

        )
        depa.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            jobs = '3',
            departamento = depa

        )
        return super(NewDepartamentoView,self).form_valid(form)


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = "departamentos"
    def get_queryset(self):
        kword = self.request.GET.get('kword','')
        lista = Departamento.objects.filter(nick__icontains=kword)
        return lista
