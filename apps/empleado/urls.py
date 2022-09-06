from django.urls import path
from . import views

urlpatterns = [
    path('listar_todo_empleados/',views.EmpleadoListView.as_view()),
    path('listar_ventas/<departamento>/',views.AreaEmpleadoListView.as_view()),
]
