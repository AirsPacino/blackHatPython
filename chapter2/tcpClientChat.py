from socket import *
import threading

ser_host = "127.0.0.1"
ser_port = 6666 

cli_sock = socket(AF_INET, SOCK_STREAM)
 
cli_sock.connect((ser_host, ser_port))


def handle_send(cli_sock):
	while True:
		command = raw_input("command~ $ ")
		cli_sock.send(command)


handler_send = threading.Thread(target=handle_send, args=(cli_sock,))
handler_send.start()
	

while True:
	response = cli_sock.recv(4096)
	print('\nReceived: ' + response)
