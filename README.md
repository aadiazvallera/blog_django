# Blog Django

Proyecto base de un blog web desarrollado con Django.

## Descripción

Este repositorio contiene la estructura inicial de un proyecto Django para construir un blog.
Incluye la configuración base del proyecto (`blog_project`) y una aplicación llamada `posts`.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/aadiazvallera/blog_django
```

Entrar a la carpeta del proyecto:

```bash
cd blog_django
```

Crear el entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual.

En Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Levantar el servidor de desarrollo:

```bash
python manage.py runserver
```

Abrir en el navegador:

```
http://127.0.0.1:8000/
```

## Aplicaciones

- `posts`: aplicación inicial para manejar las publicaciones del blog.

## Base de datos y panel de administración

El proyecto usa SQLite. El archivo `db.sqlite3` se genera localmente y no se sube al repositorio.

Después de instalar las dependencias, creá la base de datos:

```bash
python manage.py migrate
```

Creá un superusuario para entrar al panel de administración:

```bash
python manage.py createsuperuser
```

Levantá el servidor y entrá al panel:

```bash
python manage.py runserver
```

```
http://127.0.0.1:8000/admin/
```

Desde ahí se pueden crear, editar y borrar posts. Solo los posts con estado **Publicado** aparecen en la página de listado.

## Modelo Post

Campos: `titulo`, `contenido`, `autor`, `fecha_creacion` (se completa automáticamente) y `estado` (borrador, publicado o archivado).

## Páginas del sitio

- `/`: inicio.
- `/posts/`: listado de posts publicados, consultados desde la