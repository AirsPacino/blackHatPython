from socket import *

dst_host = "127.0.0.1"
dst_port = 9999

cli_sock = socket(AF_INET, SOCK_DGRAM)

cli_sock.sendto("this is a test", (dst_host, dst_port))

