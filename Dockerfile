# 1. Solución a las 42 vulnerabilidades: Pasamos de Debian antiguo a Alpine Linux.
# Alpine es una distribución minimalista enfocada en seguridad con una superficie de ataque casi nula.
FROM python:3.11-alpine

WORKDIR /app

# 2. Solución a DS-0002 (USER non-root):
# Creamos un grupo y un usuario del sistema sin privilegios.
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY app/requirements.txt .
# Usamos --no-cache-dir para no dejar archivos temporales que aumenten el tamaño de la imagen
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

# Indicamos a Docker que de aquí en adelante todo se ejecute con el usuario seguro.
USER appuser

EXPOSE 5000

# 3. Solución a DS-0026 (HEALTHCHECK):
# Le decimos a Docker que cada 30 segundos verifique si el puerto 5000 responde.
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:5000/ || exit 1

CMD ["python", "app.py"]