from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro_solicitud, name='registro_solicitud'),
    path('confirmacion/', views.confirmacion_solicitud, name='confirmacion_solicitud'),
]