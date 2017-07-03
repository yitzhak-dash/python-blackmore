import socket

import sys

target_host = "localhost"
target_port = 9999


def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # connect to our target host
        client.connect((target_host, target_port))

        if len(buffer):
            client.send(buffer)
        while True:
            # now wait for data back
            recv_len = 1
            response = ""
            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data
                if recv_len < 4096:
                    break

            print(response, )

            # wait for more input
            buffer = input("")
            buffer += '\n'

            # send it off
            client.send(buffer)
    except:
        print("[*] Exception! Exiting.")

        # tear down the connection
        client.close()


def main():
    # read in the buffer from the commandline
    # this will block, so send CTRL-D if not sending input
    # to stdin
    buffer = sys.stdin.read()
    # send data off
    client_sender(buffer)


if __name__ == '__main__':
    main()
