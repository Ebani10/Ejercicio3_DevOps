FROM python:3.9-slim
WORKDIR /app
# Copiamos todo el contenido de la carpeta app local a la carpeta app del contenedor
COPY app/ . 
CMD ["python", "programa.py", "V3.0"]