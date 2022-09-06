from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import Empleado


class EmpleadoListView(ListView):
    model = Empleado
    template_name = "empleado/list_all.html"
    

class AreaEmpleadoListView(ListView):
    #model = Empleado
    template_name = 'empleado/area_emple.html'
    

    def get_queryset(self):
        depto = self.kwargs['departamento']        
        lista = Empleado.objects.filter(departamento__name=depto)
        return lista

class EmpleadoxJobsListView(ListView):
    #model = Empleado
    template_name = 'empleado/jobs_emple.html'
    

    def get_queryset(self):
        pjobs = self.kwargs['jobs']        
        lista = Empleado.objects.filter(jobs=pjobs)
        return lista


class EmpleadosByKwordListView(ListView):
    model = Empleado
    template_name = "empleado/by_kword.html"
    context_object_name = "empleados"
    def get_queryset(self):
        print('=====================')
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(first_name=palabra_clave)
        print(lista)
        return lista
