CALCULADORA REMOTA TCP

Descripción general:
Este proyecto implementa una calculadora remota cliente-servidor utilizando sockets TCP. El objetivo es reforzar los conocimientos del protocolo TCP mediante la comunicación entre dos equipos en una misma red local. La aplicación permite realizar operaciones matemáticas básicas (+, -, *, /) entre un cliente (Windows) y un servidor (Manjaro), intercambiando datos a través de un socket TCP.

Estructura del proyecto:

server.py → Código del servidor (Manjaro)

client.py → Código del cliente (Windows)

readme.txt → Documento explicativo del funcionamiento

Servidor (server.py):
El servidor escucha conexiones entrantes en el puerto 5000, recibe del cliente tres datos (número1, operador y número2), realiza la operación solicitada, envía el resultado al cliente y cierra la conexión.
Para ejecutarlo en Manjaro:
python server.py
Salida esperada:
Servidor TCP escuchando en 0.0.0.0:5000
Conexión establecida desde ('192.168.0.10', 60542)
Conexión cerrada con ('192.168.0.10', 60542)

Cliente (client.py):
El cliente solicita al usuario dos números y un operador, se conecta al servidor en el puerto 5000, envía los datos en formato numero1,operador,numero2, recibe el resultado y lo muestra en pantalla. Luego cierra la conexión.
Para ejecutarlo en Windows:
python client.py
Ejemplo de ejecución:
Ingrese la IP del servidor: 192.168.0.105
Ingrese el primer número: 10
Ingrese la operación (+, -, *, /): *
Ingrese el segundo número: 5
Resultado: 50.0