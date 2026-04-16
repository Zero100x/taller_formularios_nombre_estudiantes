from django.db import models

class Solicitud(models.Model):
    TIPO_CHOICES = [
        ('academica', 'Académica'),
        ('administrativa', 'Administrativa'),
        ('tecnica', 'Técnica'),
        ('otra', 'Otra'),
    ]

    nombre_solicitante = models.CharField(max_length=150, verbose_name="Nombre del solicitante")
    documento_identidad = models.CharField(max_length=50, verbose_name="Documento de identidad")
    correo_electronico = models.EmailField(verbose_name="Correo electrónico")
    telefono_contacto = models.BigIntegerField(verbose_name="Teléfono de contacto")
    tipo_solicitud = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name="Tipo de solicitud")
    asunto = models.CharField(max_length=200, verbose_name="Asunto")
    descripcion_detallada = models.TextField(verbose_name="Descripción detallada")
    fecha_solicitud = models.DateField(verbose_name="Fecha de la solicitud")
    archivo_adjunto = models.FileField(upload_to='solicitudes/', blank=True, null=True, verbose_name="Archivo adjunto")

    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"

    def __str__(self):
        return f"{self.nombre_solicitante} - {self.tipo_solicitud} - {self.fecha_solicitud}"