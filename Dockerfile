# Paso 1: Usar una imagen base de Python
FROM python:3.9-slim-buster

# Paso 2: Establecer el directorio de trabajo
WORKDIR /app

# Paso 3: Copiar los requerimientos e instalarlos
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Paso 4: Copiar el código de la aplicación
COPY app/ .

# Paso 5: Exponer el puerto
EXPOSE 5000

# Paso 6: Comando para ejecutar la aplicación
CMD ["python", "app.py"]