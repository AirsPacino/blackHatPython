from socket import *

ser_host = "127.0.0.1"
ser_port = 6666 

cli_sock = socket(AF_INET, SOCK_STREAM)

cli_sock.connect((ser_host, ser_port))
cli_sock.send("this is from tcp2") 
response = cli_sock.recv(4096)
print(response)
