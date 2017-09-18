from socket import *
from threading import *

bind_ip = "127.0.0.1"
bind_port = 6666

ser_sock = socket(AF_INET, SOCK_STREAM)

ser_sock.bind((bind_ip, bind_port))

ser_sock.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))


def handle_client(client_socket):
    '''print the message the clent send'''
    request = client_socket.recv(1024)
    print("[*] Received: %s" % request)

    client_socket.send("ACK")
    client_socket.close()


''' accept() function will return the client-socket and client-addr'''
while True:
    client, addr = ser_sock.accept()
    print("[*] Accepted connection from %s:%d" % (addr[0], addr[1]))

    client_handler = Thread(target=handle_client, args=(client,))
    client_handler.start()

