# Taller Formularios Nombre Estudiantes

Proyecto desarrollado con Django para el taller de formularios. El sistema contiene dos aplicaciones independientes:

- `asistencia`: registra la asistencia de estudiantes.
- `solicitudes`: permite enviar solicitudes con archivo adjunto opcional.

Repositorio: `https://github.com/Zero100x/taller_formularios_nombre_estudiantes`

## Requisitos

- Python 3.13 o superior
- Git

## Clonar el proyecto

```bash
git clone https://github.com/Zero100x/taller_formularios_nombre_estudiantes.git
cd taller_formularios_nombre_estudiantes
```

## Crear y activar el entorno virtual

En Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activacion, puedes habilitar scripts para tu usuario con:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

## Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

## Ejecutar el servidor

```bash
python manage.py runserver
```

## Rutas disponibles

- Inicio del proyecto y formulario de asistencia: `http://127.0.0.1:8000/`
- Confirmacion de asistencia: `http://127.0.0.1:8000/confirmacion/`
- Formulario de solicitudes: `http://127.0.0.1:8000/solicitudes/`
- Confirmacion de solicitudes: `http://127.0.0.1:8000/solicitudes/confirmacion/`
- Panel de administracion: `http://127.0.0.1:8000/admin/`

## Crear un superusuario

Para ingresar al panel administrativo:

```bash
python manage.py createsuperuser
```

## Ejecutar pruebas

```bash
python manage.py test
```

Actualmente el proyecto incluye pruebas automaticas basicas para la app `asistencia`.

## Funcionalidades actuales

- Registro de asistencia mediante `ModelForm`.
- Registro de solicitudes mediante `ModelForm`.
- Almacenamiento de datos en SQLite.
- Confirmacion visual despues de enviar cada formulario.
- Carga opcional de archivos en la app `solicitudes`.
- Consulta de registros desde el panel de administracion de Django.
- Configuracion del proyecto en espanol de Colombia y zona horaria `America/Bogota`.

## Aplicaciones del proyecto

### App `asistencia`

Permite registrar:

- Nombre completo
- Documento de identidad
- Correo electronico
- Fecha de asistencia
- Hora de ingreso
- Hora de salida
- Presente
- Observaciones

### App `solicitudes`

Permite registrar:

- Nombre del solicitante
- Documento de identidad
- Correo electronico
- Telefono de contacto
- Tipo de solicitud
- Asunto
- Descripcion detallada
- Fecha de la solicitud
- Archivo adjunto opcional

## Estructura principal

```text
taller_formularios_nombre_estudiantes/
|-- asistencia/
|   |-- admin.py
|   |-- forms.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|   |-- migrations/
|   `-- templates/asistencia/
|       |-- registro.html
|       `-- confirmacion.html
|-- solicitudes/
|   |-- admin.py
|   |-- forms.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|   |-- migrations/
|   `-- templates/solicitudes/
|       |-- registro.html
|       `-- confirmacion.html
|-- taller_formularios_nombre_estudiantes/
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   `-- wsgi.py
|-- manage.py
|-- requirements.txt
`-- README.md
```

## Flujo de ramas

El repositorio se organizo con estas ramas:

- `main`: rama estable
- `develop`: rama de integracion
- `Diego`: rama de trabajo individual
- `William`: rama de trabajo individual

Ejemplo de uso:

```bash
git switch Diego
git add .
git commit -m "Describe tu cambio"
git push origin Diego
```

Luego los cambios pueden pasar a `develop` y finalmente a `main`.

## Notas

- Las apps `asistencia` y `solicitudes` estan registradas en `INSTALLED_APPS`.
- El proyecto usa SQLite por defecto.
- Los archivos adjuntos de `solicitudes` se guardan en la carpeta `media/`.

## Autor

- Diego Ceron
- Willam Inzandara
