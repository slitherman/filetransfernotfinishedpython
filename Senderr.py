import os
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("localhost", 9999))

file = open("tumblr_pz0upi3GaH1yuk3dso5_250.png", "rb")
file_size = os.path.getsize("tumblr_pz0upi3GaH1yuk3dso5_250.png")

client.send("recieved_image.png" .encode())
client.send(str(file_size).encode())

data = file.read()
client.sendall(data)
client.send(b"<END>")
file.close()
client.close()
