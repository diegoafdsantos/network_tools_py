import socket

target_host = 'www.google.com'
target_port = 80

#criar um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conectar o cliente
client.connect((target_host, target_port))

#enviar alguns dados
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receber algunsdados
response = client.recv(4096)

print(response.decode())
client.close()
