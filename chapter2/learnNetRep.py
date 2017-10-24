# *-* coding:utf-8 *-*

import sys
import getopt
import socket
import threading
import subprocess

'''some are switches, some are args'''
listen				= False
command				= False
port				= 0
target				= ""
execute				= ""
upload_dst			= ""

def usage():
	print("usage: " + '\n')
	sys.exit()

def main():
	global listen
	global port
	global target
	global command
	global execute
	global upload_dst

	if not len(sys.argv[1:]):
		usage()
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hlp:t:u:e:c",
		["help", "listen", "port", "target", "upload", "execute", "command"])
	except getopt.GetoptError as err:
		print(str(err))
		'''usage() will exit'''
		usage()

	for o, a in opts:
		if o in ('-h', 'help'):
			usage()
		elif o in ('-l', 'listen'):
			listen = True
		elif o in ('-p', 'port'):
			port = int(a)
		elif o in ('-t', 'target'):
			target = a
		elif o in ('-e', 'execute'):
			execute = a
		elif o in ('-c', 'command'):
			command = True
		elif o in ('u', 'upload'):
			upload_dst = a
		else:
			assert False, "Undefined options"


	if not listen and port > 0 and len(target):
		buffer = raw_input("command ~$ ")
		client_sender(buffer)
	if listen:
		server_loop()

def server_loop(): 
	global target
	server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	if not len(target):
		target = "0.0.0.0"

	server_sock.bind((target, port))
	server_sock.listen(5)
	
	while True:
		conn_sock, addr = server_sock.accept()
		print("[*] Listening on %s : %d" %(addr[0], addr[1]))
		client_thread = threading.Thread(target=client_handler, args=(conn_sock,))
		client_thread.start()

def client_handler(conn_sock):
	if len(upload_dst):
		print("upload_dst here!")
		try:
			file_buf = ""
			while True:
				data = conn_sock.recv(1024)
				if not len(data):
					break
				file_buf += data 
		
			file_descriptor = open(upload_dst, "wb")
			file_descriptor.write(file_buf)
			file_descriptor.close()
		
			conn_sock.send("Successful to write")
		except:
			conn_sock.send("Failed to save file")
	
	if command:
		print("command here!")
		while True:
			cmd_buffer = ""	
			cmd_buffer = conn_sock.recv(4096)

			print("cmd_buffer: " + cmd_buffer)
			output = run_command(cmd_buffer)
			print(output)
			conn_sock.send(output)
				
		
	if len(execute):
		print("execute here!")
		output = run_command(execute)
		conn_sock.send(output)

def run_command(execute):

	print("run_command here!")
	execute = execute.rstrip()
	print(execute)
	try:
		output = subprocess.check_output(execute, shell=True)
	except:
		output = "Fail to execute command\n"
	return output


def client_sender(buffer):
	client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_sock.connect((target, port))
	if len(buffer):
		client_sock.send(buffer)
		while True:
			'''reset the response when it sent new message'''
			response = ""
			while True:
				data = client_sock.recv(4096)
				len_recv = len(data)
				response = response + data

				if len_recv < 4096:
					break

			print(response)
			buffer = raw_input("command ~$ ")
			client_sock.send(buffer)
	client_sock.close()

	




if __name__ == '__main__':
	main()
