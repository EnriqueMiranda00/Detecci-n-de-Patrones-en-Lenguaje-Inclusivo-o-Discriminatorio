
# ACREDICOM - Gestor de Tareas (Django + SQLite)

Proyecto de ejemplo con Django 5, SQLite, Bootstrap 5 y AJAX para gestionar **tareas** con **roles** (Administrador/Usuario). El Administrador puede asignar tareas a usuarios, y los usuarios solo ven las suyas. Incluye login, logout y recuperación de contraseña (por consola en desarrollo).

## Requisitos
- Python 3.10+
- pip

## Instalación (Windows / PowerShell)
```ps1
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Accede a `http://127.0.0.1:8000/`.

## Roles
- Se crean los grupos `ADMINISTRADOR` y `USUARIO` automáticamente.
- Cualquier usuario nuevo pertenece por defecto a `USUARIO`.
- Desde **Usuarios** (solo admin) puedes cambiar el rol.

## Módulos
- **Tareas**: CRUD solo para Administrador; los Usuarios ven solo sus tareas. Cambio de estado vía AJAX.
- **Usuarios**: CRUD solo para Administrador (username, email, nombres completos, rol, activo).

## Estilo
- Tema verde ACREDICOM (navbar, botones, textos principales).

## Notas
- Recuperación de contraseña usa backend de consola: verás el enlace en la terminal donde corre `runserver`.
- Base de datos: `db.sqlite3` en el root del proyecto.
```
