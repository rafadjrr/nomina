from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.IndexView.as_view()),
    path('listar/',views.PruebaListView.as_view()),
    path('prueba/',views.ModelPruebaListView.as_view()),
    path('add/',views.PruebaCreateView.as_view(), name="prueba_add"),
]