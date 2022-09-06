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