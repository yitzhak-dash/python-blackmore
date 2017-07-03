import socket
import threading

bind_ip = "localhost"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print("[*] listen on {0}:{1}".format(bind_ip, bind_port))


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("received from client: {0}".format(request))
    client_socket.send("ACK YOU!!!")


while True:
    client, addr = server.accept()
    print("[*] Accepted connection from: {0}:{1}".format(addr[0], addr[1]))

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
