from django.urls import path
from . import views

app_name = "empleado_app"

urlpatterns = [
    path('',views.InicioView.as_view(),name='inicio'),
    path('listar_empleados/',views.EmpleadoListView.as_view(),name='empleados_all'),
    path('listar_area_emple/<departamento>/',views.AreaEmpleadoListView.as_view(),name='empleados_area'),
    path('listar_jobs/<jobs>/',views.EmpleadoxJobsListView.as_view()),
    path('buscar_empleado/',views.EmpleadosByKwordListView.as_view()),
    path('buscar_empleado_x_habilidades/<id>/',views.HabilidadesEmpleadosListView.as_view()),
    path('ver_empleado/<pk>/',views.EmpleadoDetailView.as_view(),name='empleado_detail'),
    path('crear_empleado/',views.EmpleadoCreateView.as_view()),
    path('success/',views.SuccessTemplateView.as_view(), name='success'),
    path('update_empleado/<pk>/',views.EmpleadoUpdateView.as_view(), name='update'),
    path('delete_empleado/<pk>/',views.EmpleadoDeleteView.as_view(), name='delete')
]
