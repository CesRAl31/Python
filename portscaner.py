#Programa básico para escanear los puertos abiertos o cerrados de tu red
import socket

ip = input("Ingrese la dirección IP a escanear: ")

for puerto in range(1, 65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Sock especifica la posibilidad de hacer conexiones
    #Socket.AF_INET da la forma de la ip 192.168.1.xx , socket.SOCK_STREAM especifica el protocolo IP

    sock.settimeout(5)

    result = sock.connect_ex((ip, puerto))

    if result == 0:
        print("Puerto abierto: " + str(puerto))
        sock.close()
    else: 
        print("puerto cerrado: " + str(puerto))