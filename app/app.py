from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.get('/')
def hola():
    user_agent = request.headers.get('User-Agent', 'Desconocido')
    
    # SOLUCIÓN AL SSTI/XSS: En lugar de render_template_string con f-strings,
    # pasamos la variable como un argumento limpio para que Jinja2 la sanitice automáticamente.
    # Para mantenerlo simple sin archivos HTML externos, usamos una plantilla inline segura,
    # pero pasándole el parámetro de forma correcta.
    return render_template_string("<h1>Hola Mundo desde Flask!</h1><p>Tu User-Agent es: {{ ua }}</p>", ua=user_agent)

if __name__ == '__main__':
    # SOLUCIÓN AL HOST Y DEBUG: Leemos los valores desde variables de entorno.
    # Por defecto, si no se definen, usamos valores seguros para producción ('127.0.0.1' y False).
    # En desarrollo local vía Docker Compose, inyectaremos los valores necesarios.
    HOST = os.environ.get('FLASK_HOST', '127.0.0.1')
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    
    app.run(host=HOST, port=5000, debug=DEBUG)