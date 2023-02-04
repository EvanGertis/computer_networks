import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))
print(type("I am CLIENT\n"))
client.send(bytearray("I am CLIENT\n",'utf-8'))

from_server = client.recv(4096)

client.close()

print(from_server)
