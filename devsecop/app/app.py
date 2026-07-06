from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# --- INICIO DEL ERROR DE SEGURIDAD (Vulnerabilidad SAST) ---
# En una aplicación real, NUNCA debes dejar secretos hardcodeados en el código.
# Esto es exactamente lo que Semgrep buscará.
SUPER_SECRET_API_KEY = "12345-mi-secreto-super-inseguro"
# --- FIN DEL ERROR DE SEGURIDAD ---

@app.get('/')
def hola():
    user_agent = request.headers.get('User-Agent')
    return render_template_string(f"<h1>Hola Mundo desde Flask!</h1><p>Tu User-Agent es: {user_agent}</p>")

if __name__ == '__main__':
    # Corremos la app de forma insegura y en el puerto 5000
    app.run(host='0.0.0.0', port=5000, debug=True)