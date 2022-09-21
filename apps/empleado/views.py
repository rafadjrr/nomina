
from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,TemplateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
from .models import Empleado


class EmpleadoListView(ListView):
    model = Empleado
    template_name = "empleado/list_all.html"
    paginate_by = 3
    ordering = '-first_name'
    

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
        return lista


class HabilidadesEmpleadosListView(ListView):
    model = Empleado
    template_name = "empleado/habilidades.html"
    context_object_name = "habilidades"
    def get_queryset(self):
        pclave = self.kwargs['id']
        empleado = Empleado.objects.get(id=pclave)
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo']='Empleado del mes'
        return context


class SuccessTemplateView(TemplateView):
    template_name = "empleado/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/create.html"
    #fields = ("__all__")
    fields = [
        'first_name',
        'last_name',
        'jobs',
        'departamento',
        'habilidades',
        'historia',
    ]
    success_url = reverse_lazy("empleado_app:success")
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado/empleado_update.html"
    fields = [
        'first_name',
        'last_name',
        'jobs',
        'departamento',
        'habilidades',
        'historia',
    ]
    success_url = reverse_lazy("empleado_app:success")
    def form_valid(self, form):
        return super().form_valid(form)
    def post(self, request, *args, **kwargs):
        return super(EmpleadoUpdateView,self).post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/delete.html"
    success_url = reverse_lazy("empleado_app:success")


class InicioView(TemplateView):
    template_name = "inicio.html"
    