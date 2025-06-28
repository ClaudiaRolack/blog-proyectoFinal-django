# 📝 Blog Proyecto Final - Django

Este es un blog desarrollado con Django como proyecto final del curso de programación con Python. Permite a los usuarios registrarse, iniciar sesión, crear categorías y posts, comentar, buscar contenido por palabra clave o categoría, y gestionar completamente sus publicaciones y comentarios.


## 🚀 Funcionalidades principales

- Registro e inicio de sesión de usuarios.
- Creación, edición y eliminación de posts personales.
- Creación, edición y eliminación de comentarios.
- Creación de categorías personalizadas.
- Prevención de categorías duplicadas (ignora mayúsculas/minúsculas).
- Visualización de publicaciones filtradas por categoría.
- Búsqueda por palabra clave o nombre de categoría.
- Vista de "Sobre nosotros" que explica el propósito del blog.
- Expiración de sesión tras 1 hora de inactividad.

## 🧱 Estructura del proyecto

![Estructura del proyecto](assets/estructuraBlog.png)


## 🗃️ Diagrama de la base de datos

![Diagrama de la base de datos](assets/diagramaBlog.png)


## ⚙️ Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/ClaudiaRolack/blog-proyectoFinal-django.git
   cd blog-proyectoFinal-django/proyectoFinal

2. Crea un entonor virtual e instala las dependencias:

   ```bash
   python -m venv env
   .venv\Scripts\Activate.ps1 
   pip install -r requirements.txt

3. Aplica las migraciones y crea un superusuario:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser

4. Ejecuta el servidor:

   ```bash
   python manage.py runserver

5. Abre tu navegador en http://127.0.0.1:8000/


## 🧪 Cómo usar la app

1. **Registrate** desde la página principal.
2. **Inicia sesión** con tus credenciales.
3. **Crea una categoría** en la sección correspondiente.
4. **Escribe un post**, eligiendo una o varias categorías.
5. **Explora tus posts** en "Mis posts".
6. **Edita o elimina tus publicaciones** desde el listado personal.
7. **Comenta en cualquier post** y gestiona tus propios comentarios.
8. **Busca contenido** desde el input de búsqueda (por palabra clave o nombre de categoría).
9. **Haz clic en una categoría** para ver todos los posts asociados.
10. **Consulta la sección "Sobre nosotros"** para más información del proyecto.


## 🔐 Seguridad y configuración

- Las sesiones expiran tras 1 hora de inactividad: configurado con SESSION_COOKIE_AGE = 3600 en settings.py.
- Los formularios están protegidos contra ataques CSRF.
- Solo los usuarios autenticados pueden crear contenido o comentar.
- Solo el autor de un post o comentario puede editar o eliminarlo.


## ✅ Requisitos

- Python 3.9+
- Django 5.x
- SQLite (base de datos por defecto)


---


# 💡 ¡Gracias por visitar el proyecto!