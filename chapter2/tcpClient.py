from socket import *

ser_host = "www.baidu.com"
ser_port = 80 

cli_sock = socket(AF_INET, SOCK_STREAM)

cli_sock.connect((ser_host, ser_port))
cli_sock.send("GET / HTTP/1.1\r\nHost:baidu.com\r\n\r\n") 
response = cli_sock.recv(4096)
print(response)
