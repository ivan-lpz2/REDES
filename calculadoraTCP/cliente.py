import socket  # Importa la librería 'socket' para permitir la comunicación en red (TCP/IP)

# Se solicita al usuario la dirección IP del servidor al que se conectará
SERVER_IP = input("Ingrese la IP del servidor: ")

# Puerto en el que el servidor está escuchando (debe coincidir con el del servidor)
PORT = 5000

# Se piden los dos números y el operador que el servidor debe procesar
num1 = input("Ingrese el primer número: ")
operador = input("Ingrese la operación (+, -, *, /): ")
num2 = input("Ingrese el segundo número: ")

# Se crea un socket con:
# AF_INET → indica que se usará el protocolo IPv4
# SOCK_STREAM → indica que se usará el protocolo TCP (orientado a conexión)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se establece la conexión con el servidor usando la IP y el puerto proporcionados
client_socket.connect((SERVER_IP, PORT))

# Se construye un mensaje en formato texto con los datos separados por comas
# Ejemplo: "8,+,5"
mensaje = f"{num1},{operador},{num2}"

# El mensaje se codifica a bytes y se envía al servidor mediante el socket
client_socket.send(mensaje.encode())

# Se espera la respuesta del servidor (máximo 1024 bytes)
# recv() devuelve los datos en formato bytes, por lo que se decodifican a texto con decode()
resultado = client_socket.recv(1024).decode()

# Se muestra el resultado recibido desde el servidor
print(f"Resultado: {resultado}")

# Se cierra el socket para liberar los recursos de red
client_socket.close()

