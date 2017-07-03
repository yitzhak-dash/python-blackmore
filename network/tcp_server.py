import socket
import threading

import subprocess


def server_loop():
    bind_ip = "localhost"
    bind_port = 9999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((bind_ip, bind_port))

    server.listen(5)

    print("[*] listen on {0}:{1}".format(bind_ip, bind_port))

    while True:
        client_socket, addr = server.accept()
        print("[*] Accepted connection from: {0}:{1}".format(addr[0], addr[1]))

        # spin up our client thread to handle incoming data
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()


def run_command(command):
    # trim the newline
    command = command.rstrip()

    # run the command and get the output back
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = "Failed to execute the command: {0}.\r\n".format(command)
    # send the output to the client
    return output


def client_handler(client_socket):
    while True:
        # show a simple prompt
        client_socket.send("<BHP:#> ")
        # now we receive until we see a linefeed (enter key)
        cmd_buffer = ""
        while "\n" not in cmd_buffer:
            cmd_buffer += client_socket.recv(1024)
        # send back the command output
        response = run_command(cmd_buffer)
        # send back the response
        client_socket.send(response)


def main():
    server_loop()


if __name__ == '__main__':
    main()
