Cree a traves de docker compose, un contenedor servidor que espera a recibir comandos de uno o mas contenedores cliente para ejecutarlos y enviarles informacion de acuerdo al comando.
Los contenedores cliente enviaran los comandos de forma manual al entrar en ellos.

Los comandos de ejemplo que podran enviar los clientes seran:
cliente> lsFiles     // nos regresara el listado de los archivos que se encuentran en el folder de "Files" en la misma ruta donde se esta ejecutando el servidor.
Dentro de la carpeta files tendremos:
- archivo.txt
- movies.json
...
cliente>get archivo.txt  // el servidor debera enviar el achivo al cliente, el cliente debera crear un folder "download" y guardar el archivo ahi mismo.

Es importante recordar que enviar un comando no debera replicarse a los demas clientes conectados, solo a quien lo envia.
-----------------------------------
Ejecutamos docker-compose up --build
![imagen](https://github.com/user-attachments/assets/3680da4b-cb0c-4aea-b142-3f1844c2fc08)

![imagen](https://github.com/user-attachments/assets/5675ff9d-9a33-4754-8176-ba6c45755093)

una vez con los contenedores corriendo, entramos al servidor con ``docker exec -it server bash`` y lo iniciamos

![imagen](https://github.com/user-attachments/assets/4cac0bc9-b2de-41fb-b8a9-79060e069696)

luego entramos al cliente1 con ``docker exec -it client1 bash`` ejecutamos el script y nos conectara con el servidor donde podremos enviar comandos
![imagen](https://github.com/user-attachments/assets/cd73cb88-58f4-46af-894f-e152471ec8b6)
Haciendo pruebas podemos ver que el servidor atiende a varios clientes de manera separada
![imagen](https://github.com/user-attachments/assets/413092a0-4c35-4a31-a648-b21a628c1b2c)


