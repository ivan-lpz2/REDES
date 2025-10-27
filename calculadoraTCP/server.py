import socket

# Configuración del servidor
HOST = "0.0.0.0"   # Escucha en todas las interfaces de red
PORT = 5000        # Puerto de escucha

# Crear el socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor TCP escuchando en {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Conexión establecida desde {addr}")

    # Recibir los datos enviados por el cliente
    data = conn.recv(1024).decode()

    if not data:
        break

    # Los datos vienen en formato: "numero1,operador,numero2"
    try:
        num1, operador, num2 = data.split(",")
        num1 = float(num1)
        num2 = float(num2)

        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: división por cero"
        else:
            resultado = "Operador inválido"

    except Exception as e:
        resultado = f"Error al procesar: {e}"

    # Enviar el resultado al cliente
    conn.send(str(resultado).encode())
    conn.close()
    print(f"Conexión cerrada con {addr}\n")
