# Taller Formularios Nombre Estudiantes

Proyecto desarrollado con Django para gestionar formularios academicos. En esta primera parte se implemento la app `asistencia`, que permite registrar la asistencia de estudiantes mediante un formulario web y administrar la informacion desde el panel de Django.

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

Luego abre en el navegador:

- Formulario de asistencia: `http://127.0.0.1:8000/`
- Panel de administracion: `http://127.0.0.1:8000/admin/`

## Crear un superusuario

Para ingresar al panel administrativo:

```bash
python manage.py createsuperuser
```

## Funcionalidades actuales

- Registro de asistencia con formulario web.
- Validacion de campos desde Django Forms.
- Confirmacion visual despues de guardar el registro.
- Administracion de asistencias desde el panel de Django.
- Base de datos SQLite configurada por defecto.

## Estructura principal

```text
taller_formularios_nombre_estudiantes/
|-- asistencia/
|   |-- admin.py
|   |-- forms.py
|   |-- models.py
|   |-- urls.py
|   |-- views.py
|   `-- templates/asistencia/
|       |-- registro.html
|       `-- confirmacion.html
|-- taller_formularios_nombre_estudiantes/
|   |-- settings.py
|   `-- urls.py
|-- manage.py
`-- requirements.txt
```

## Modelo principal

La app `asistencia` almacena:

- Nombre completo
- Documento de identidad
- Correo electronico
- Fecha de asistencia
- Hora de ingreso
- Hora de salida
- Estado de presencia
- Observaciones

## Notas

- El proyecto esta configurado con idioma `es-co` y zona horaria `America/Bogota`.
- La app `solicitudes` podra agregarse despues sin romper la configuracion actual del proyecto.

## Autor

Diego Ceron
