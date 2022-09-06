from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Empleado)
class Admin(admin.ModelAdmin):

    '''Admin View for '''
    def full_name(self,obj):
        #print(obj.first_name)
        return obj.first_name +' '+ obj.last_name

    list_display = ('first_name','last_name','jobs','full_name','historia','departamento')
    list_filter = ('jobs','habilidades','departamento')
    filter_horizontal = ('habilidades',)
    #raw_id_fields = ('',)
    #readonly_fields = ('',)
    search_fields = ('jobs',)
    #date_hierarchy = ''
    ordering = ('first_name',)

@admin.register(Habilidad)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name',)
    list_filter = ('name',)
    #raw_id_fields = ('name',)
    #readonly_fields = ('id')
    search_fields = ('name',)
    ordering = ('-name',)