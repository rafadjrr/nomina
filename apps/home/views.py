from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *

class IndexView(TemplateView):
    template_name = 'home/home.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['A','B','C']
    context_object_name = 'lista_prueba'

#class ModelPruebaListView(ListView):

class ModelPruebaListView(ListView):
    model = Prueba
    template_name = "home/prueba.html"
    context_object_name = 'lista_prueba'