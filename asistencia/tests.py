from datetime import date, time

from django.test import TestCase
from django.urls import reverse

from .models import Asistencia


class AsistenciaModelTests(TestCase):
    def test_str_muestra_nombre_y_fecha(self):
        asistencia = Asistencia.objects.create(
            nombre_completo='Diego Ceron',
            documento_identidad='1234567890',
            correo_electronico='diego@example.com',
            fecha_asistencia=date(2026, 4, 16),
            hora_ingreso=time(8, 0),
            hora_salida=time(12, 0),
            presente=True,
            observaciones='Registro de prueba',
        )

        self.assertEqual(str(asistencia), 'Diego Ceron - 2026-04-16')


class AsistenciaViewsTests(TestCase):
    def test_registro_asistencia_renderiza_formulario(self):
        response = self.client.get(reverse('registro_asistencia'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'asistencia/registro.html')
        self.assertIn('form', response.context)

    def test_registro_asistencia_guarda_y_redirige(self):
        response = self.client.post(reverse('registro_asistencia'), data={
            'nombre_completo': 'Diego Ceron',
            'documento_identidad': '1234567890',
            'correo_electronico': 'diego@example.com',
            'fecha_asistencia': '2026-04-16',
            'hora_ingreso': '08:00',
            'hora_salida': '12:00',
            'presente': 'on',
            'observaciones': 'Prueba desde test',
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('confirmacion_asistencia'))
        self.assertEqual(Asistencia.objects.count(), 1)

    def test_confirmacion_asistencia_renderiza_template(self):
        response = self.client.get(reverse('confirmacion_asistencia'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'asistencia/confirmacion.html')
