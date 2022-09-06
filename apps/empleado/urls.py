from django.urls import path
from . import views

urlpatterns = [
    path('listar_todo_empleados/',views.EmpleadoListView.as_view()),
    path('listar_ventas/<departamento>/',views.AreaEmpleadoListView.as_view()),
    path('listar_jobs/<jobs>/',views.EmpleadoxJobsListView.as_view()),
    path('buscar_empleado/<jobs>/',views.EmpleadosByKwordListView.as_view())
]
