from django.contrib import admin
from django.urls import path

from . import views
app_name = "dpto_app"
urlpatterns = [
    path('new/', views.NewDepartamentoView.as_view(), name='newdpto'),
    path('list/', views.DepartamentoListView.as_view(), name='listdpto')
]

