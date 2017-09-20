# _*_ coding: utf-8 _*_
# replace the netcat(nc)

import sys
import socket
import getopt
import threading
import subprocess

# define some global variables
listen				= False
command				= False
upload				= False
execute				= ""
target				= ""
upload_destination	= ""
port				= 0

def usage():
	print("BHP Net Tool")
	print("")
	print("Usage: netcatREP.py -t target_host -p port")
	print("-l --listen			- listen on [host]:[port] for incoming connections")
	print("-e --execute=file_to_run")
	print("-c --commandshell")
	print("-u --upload=destination")
	print("-t --target=target_host")
	print("-p --port=integar")
	print("Examples: ")
	print("")
	print("")
	print("")
	sys.exit(0)

def main():
	global listen
	global port
	global execute
	global command
	global upload_destination
	global target

	if not len(sys.argv[1:]):
		usage()

	''' read the commandline options '''
	try:
		''' getopt() return two lists '''
		opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",
		["help", "listen", "execute", "target", "port", "command", "upload"])
	except getopt.GetoptError as err:
		print(str(err))
		usage()

	for o, a in opts:
		if o in ("-h", "--help"):
			usage()
		elif o in ("-l", "--listen"):
			listen = True
		elif o in ("-e", "--execute"):
			execute = a
		elif o in ("-c", "--commandshell"):
			command = True
		elif o in ("-u", "--upload"):
			upload_destination = a
		elif o in ("-t", "--target"):
			target = a
		elif o in ("-p", "--port"):
			port = int(a)
		else:
			assert False, "Unhandled Option"

	if not listen and len(target) and port > 0:
		buffer = sys.stdin.read()
		client_sender(buffer)

	if listen:
		server_loop()

def client_sender(buffer):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:	
		client.connect((target, port))
			
		if len(buffer):
			client.send(buffer)

			while True:
				len_recv = 1	
				response = ""

				while len_recv:
					recv_data = client.recv(4096)
					len_recv = len(recv_data)
					response = recv_data + response 

					if len_recv < 4096:
						break

				print('\n' + response)
				buffer = raw_input("please enter: ")
				buffer = buffer + '\n'
				client_send(buffer)
						
	except:
		print("[*] Excepting, exiting...")
		client.close()

def server_loop():
	global target
	global port
		
	if not len(target):
		target = '0.0.0.0'
			
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((target, port))
	server.listen(5)
	print("[*] Server Listening on %s:%d" % (target, port))


	while True:
		client, addr = server.accept()
		print("[*] client addr:%s, clinet port:%d" %(addr[0], addr[1]))
		handler = threading.Thread(target=client_handler, args=(client,))
		handler.start()

def run_command(command):

	command = command.rstrip()
	try:
		output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
	except:
		output = "Failed to excute command.\r\n"
	return output

def client_handler(client_socket):
	global upload
	global execute
	global command
	

	if len(upload_destination):
		file_buffer = ""

		while True:
			data = client_socket.recv(4096)
			
			if data == 'exit':
				break
			else:
				data = data + '\n[*] '
				file_buffer += data
				print("[*] file_buffer: " + file_buffer)

		try:
			file_descriptor = open(upload_destination, "wb")
			file_descriptor.write(file_buffer)
			file_descriptor.close()

			client_socket.send("Successfully saved file to %s\r\n" % upload_destination)
		except:
			client_socket.send("Failed to save file to %s\r\n" %upload_destination)

		print "will exit..."
	if len(execute):
		print("I'm in execute")
		print("execute: " + execute)
		output = run_command(execute)
		client_socket.send(output)

	if command:
		
		print("I'm in command")
		while True:

			client_socket.send("<BHP:#>")
			cmd_buffer = ""

			while '\n' not in cmd_buffer:

				cmd_buffer = client_socket.recv(1024)
				print("cmd_buffer: " + cmd_buffer)
				response = run_command(cmd_buffer)
				client_socket.send(response)


if __name__ == "__main__":
	 main()
