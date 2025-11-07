
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario_asignado', 'prioridad', 'estado', 'fecha_vencimiento', 'fecha_creacion')
    list_filter = ('prioridad', 'estado', 'usuario_asignado')
    search_fields = ('titulo', 'descripcion')
