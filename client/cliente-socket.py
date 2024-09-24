import socket
import threading
import pickle
import os

class Cliente():
    def __init__(self, host="server", port=7000):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, port))
            msg_recv = threading.Thread(target=self.msg_recv)
            msg_recv.daemon = True
            msg_recv.start()
            while True:
                msg = input('-> ')
                if msg != 'salir':
                    self.send_msg(msg)
                else:
                    self.sock.close()
                    break
        except Exception as e:
            print(f"Error al conectar al socket: {e}")
            
    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    response = pickle.loads(data)
                    if isinstance(response, dict) and "filename" in response:
                        self.guardar_archivo(response["filename"], response["data"])
                    else:
                        print(response)  # Imprimir respuesta
                else:
                    break
            except Exception as e:
                print(f"Error al recibir mensaje: {e}")
                break

    def send_msg(self, msg):
        try:
            self.sock.send(pickle.dumps(msg))
        except Exception as e:
            print(f'Error al enviar el mensaje: {e}')

    def guardar_archivo(self, filename, data):
        download_dir = "download"
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        filepath = os.path.join(download_dir, filename)
        with open(filepath, "wb") as f:
            f.write(data)
        print(f"Archivo {filename} guardado en {download_dir}")

if __name__ == "__main__":
    Cliente()
