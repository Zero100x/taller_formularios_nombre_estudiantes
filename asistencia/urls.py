from django.urls import path

from . import views

urlpatterns = [
    path('', views.registro_asistencia, name='registro_asistencia'),
    path('confirmacion/', views.confirmacion_asistencia, name='confirmacion_asistencia'),
]
