from atexit import register
from django.contrib import admin
from .models import Departamento

# Register your models here.
@admin.register(Departamento)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name','estatus',)
    list_filter = ('name','estatus',)
    #inlines = [
    #    Inline,
    #]
    #raw_id_fields = ('',)
    #readonly_fields = ('',)
    #search_fields = ('',)
    #date_hierarchy = ''
    #ordering = ('',)