from django.contrib import admin

from .models import Asistencia


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'documento_identidad', 'fecha_asistencia', 'presente']
    list_filter = ['presente', 'fecha_asistencia']
    search_fields = ['nombre_completo', 'documento_identidad']
