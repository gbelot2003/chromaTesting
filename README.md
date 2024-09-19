# Aplicación de Chat con DeepSeek API y Flask

Este proyecto es una aplicación web desarrollada en Flask que permite la comunicación con la API de DeepSeek a través de WebSockets. La aplicación está diseñada para ser modular, facilitando la escalabilidad y el mantenimiento del código.

## Estructura del Proyecto
/mi_app_flask
/app
init.py
/routes
init.py
chat.py
/services
init.py
deepseek_service.py
/utils
init.py
websocket_utils.py
/templates
index.html
/static
/css
styles.css
/js
chat.js
run.py

Copy code

## Requisitos

- Python 3.7 o superior
- Flask
- Flask-SocketIO
- Requests

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install Flask Flask-SocketIO requests
```

Configuración
Paso 1: Configuración de la Aplicación Flask
El archivo app/__init__.py configura la aplicación Flask y la inicialización de SocketIO.

Paso 2: Definición de Rutas
El archivo app/routes/chat.py define las rutas y los manejadores de eventos para el chat.

Paso 3: Servicio para Comunicarse con DeepSeek API
El archivo app/services/deepseek_service.py contiene la lógica para comunicarse con la API de DeepSeek.

Paso 4: Utilidades para WebSockets
El archivo app/utils/websocket_utils.py proporciona funciones auxiliares para manejar mensajes a través de WebSockets.

Paso 5: Archivos Estáticos y Plantillas
templates/index.html: Plantilla HTML para la interfaz de chat.

static/css/styles.css: Archivo CSS para estilos de la interfaz.

static/js/chat.js: Archivo JavaScript para manejar la lógica del chat en el lado del cliente.

Paso 6: Ejecutar la Aplicación
El archivo run.py inicia la aplicación Flask con SocketIO.

Ejecución
Para ejecutar la aplicación, simplemente ejecuta el archivo run.py:

```bash
python run.py
```
Luego, puedes acceder a la aplicación en http://localhost:5000 y comenzar a chatear con la API de DeepSeek a través de WebSockets.

Notas
Asegúrate de reemplazar 'YOUR_API_KEY' en deepseek_service.py con tu clave de API real de DeepSeek.

Verifica que la URL de la API de DeepSeek sea correcta y que tengas acceso a ella.

Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna sugerencia, por favor abre un issue o envía un pull request.

Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.