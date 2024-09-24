import socket
import threading
import os
import pickle

class Servidor():
    def __init__(self, host="0.0.0.0", port=7000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(5)
        print("Servidor iniciado y esperando conexiones...")
        self.files_dir = "Files"
        self.iniciar()

    def iniciar(self):
        while True:
            conn, addr = self.sock.accept()
            print(f"Conexión aceptada de {addr}")
            threading.Thread(target=self.handle_client, args=(conn,)).start()

    def handle_client(self, conn):
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    print("Cliente desconectado.")
                    break  # Salir si el cliente se desconecta
                msg = pickle.loads(data)
                print(f"Comando recibido: {msg}")
                respuesta = self.procesar_comando(msg)
                conn.send(pickle.dumps(respuesta))  # Enviar respuesta al cliente
            except Exception as e:
                print(f"Error al manejar el cliente: {e}")
                break
        conn.close()  # Cerrar la conexion cuando se termine el hilo

    def procesar_comando(self, msg):
        if msg == "lsFiles":
            archivos = os.listdir(self.files_dir)
            return archivos
        elif msg.startswith("get "):
            archivo_solicitado = msg.split(" ")[1]
            ruta_archivo = os.path.join(self.files_dir, archivo_solicitado)
            if os.path.exists(ruta_archivo):
                with open(ruta_archivo, "rb") as f:
                    contenido = f.read()
                return {"filename": archivo_solicitado, "data": contenido}
            else:
                return f"El archivo {archivo_solicitado} no existe"
        else:
            return "Comando no reconocido"

if __name__ == "__main__":
    Servidor()
