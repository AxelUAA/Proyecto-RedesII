# Imagen base de Python
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos
COPY app.py /app/

# Instalar Flask
RUN pip install flask

# Exponer el puerto del backend
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
