import socket

target_host = "localhost"
target_port = 9999

# create a socket object
# AF_INET - use standard IP4v
# SOCK_STREAM - a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
data = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(str(data).upper().encode())

# receive some data
response = client.recv(4096)

print(str(response))
