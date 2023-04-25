## PROYECTO_FINAL_CODER

Link a video tutorial: https://www.youtube.com/watch?v=ZCvByVAV614

DESCRIPCION
Este es un proyecto utilizando Python y el framework Django para crear un blog. El proyecto se divide en diferentes aplicaciones las cuales tienen sus tareas especificas. La primera aplicacion seria 'App_Accounts', la cual maneja el registro y logueo de usuarios a la vez que les crea un perfil en la pagina, el cual pueden eliminar y editar a su gusto. Al estar logueados tiene acceso a las dos siguientes aplicaciones, 'App_Messages' y 'App1', que se encargan de permitir a los usuarios enviarse mensajes entre si y de manejar la feed del los blogs subidos por los usuarios respectivamente. Finalmente la aplicacion 'App_About' solo maneja la plantilla donde se muestra la informacion sobre el autor del proyecto.

INSTALACION
.Primero, debes clonar el repositorio en tu máquina local utilizando el siguiente comando: git clone https://github.com/tu-usuario/PROYECTO_FINAL_CODER.git
Asegúrate de reemplazar tu-usuario con tu nombre de usuario de GitHub.

.Luego, entra en la carpeta del proyecto: cd PROYECTO_FINAL_CODER

.Crea un entorno virtual utilizando el siguiente comando: python -m venv env

.Activa el entorno virtual utilizando el siguiente comando en Windows: env\Scripts\activate.bat

.O el siguiente comando en Mac o Linux: source env/bin/activate

.Instala las dependencias del proyecto utilizando el siguiente comando: pip install -r requirements.txt

.Crea una base de datos utilizando el siguiente comando: python manage.py migrate

.Crea un superusuario para tener acceso a la interfaz de administración utilizando el siguiente comando: python manage.py createsuperuser

.Sigue las instrucciones para crear un nombre de usuario y contraseña.

.Puedes iniciar el servidor de desarrollo utilizando el siguiente comando: python manage.py runserver

.Para acceder al sitio web, abre tu navegador y navega a http://localhost:8000/. Para acceder a la interfaz de administración, navega a http://localhost:8000/admin/ y usa las credenciales del superusuario que creaste.


USO

.Registro y login:
Para crear una cuenta, los usuarios deben hacer clic en el botón "Registrarse" y proporcionar los datos que se requieran. Luego, deben hacer clic en "Registrarse" y los usuarios pueden iniciar sesión en la página utilizando su nombre de usuario y contraseña.

.Edición del perfil:
Una vez que los usuarios han iniciado sesión, pueden acceder a la página de perfil y editar su información. Los usuarios pueden agregar una imagen de perfil y actualizar su información personal, como su nombre, correo electrónico y link a alguna pagina web.

.Envío de mensajes:
Los usuarios pueden enviar mensajes entre ellos utilizando la aplicación 'App_Messages'. Para enviar un mensaje, el usuario debe estar logueado y navegar a la sección de mensajes. Allí pueden seleccionar al destinatario del mensaje y escribir el mensaje en el formulario.

.Feed de blogs:
La aplicación 'App1' maneja la feed de los blogs subidos por los usuarios. Para publicar un blog, el usuario debe estar logueado y navegar a la sección de "Crear nuevo blog". Luego, pueden escribir el título y el contenido del blog y publicarlo. Los usuarios también pueden ver los blogs publicados por otros usuarios en la página de Blogs.

.Información sobre el autor:
La aplicación 'App_About' muestra la información sobre el autor del proyecto en una página de Sobre mi.

.Interfaz de administración:
Los superusuarios tienen acceso a la interfaz de administración, donde pueden agregar, editar o eliminar contenido y usuarios del sitio web. Para acceder a la interfaz de administración, el superusuario debe iniciar sesión y navegar a http://localhost:8000/admin/.

AUTORES
Alejo Gutierrez
alejogutierrez02@gmail.com

