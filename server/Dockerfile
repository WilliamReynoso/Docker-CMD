FROM python:3.12-slim
WORKDIR /app
COPY server-socket.py /app
RUN mkdir Files

# Agrega algunos archivos de ejemplo
RUN echo "Contenido del archivo.txt" > Files/archivo.txt
RUN echo '{"movies": ["movie1", "movie2"]}' > Files/movies.json
# Ejecutar el servidor
# CMD ["python", "server-socket.py"] Las pruebas se haran de forma manual
