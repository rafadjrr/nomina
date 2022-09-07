from django.urls import path
from . import views

urlpatterns = [
    path('listar_todo_empleados/',views.EmpleadoListView.as_view()),
    path('listar_ventas/<departamento>/',views.AreaEmpleadoListView.as_view()),
    path('listar_jobs/<jobs>/',views.EmpleadoxJobsListView.as_view()),
    path('buscar_empleado/',views.EmpleadosByKwordListView.as_view()),
    path('buscar_empleado_x_habilidades/<id>/',views.HabilidadesEmpleadosListView.as_view()),
    path('ver_empleado/<pk>/',views.EmpleadoDetailView.as_view())
]
