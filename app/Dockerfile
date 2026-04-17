# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Creamos una carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de nuestro proyecto al contenedor
COPY programa.py .
COPY lista.txt .

# Comando que se ejecutará al iniciar el contenedor
CMD ["python", "programa.py"]