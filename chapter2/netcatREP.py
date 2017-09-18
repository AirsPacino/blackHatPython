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
		if o in ("h", "--help"):
			usage()
		elif o in ("l", "--listen"):
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
'''
	if not listen and len(target) and port > 0:
		buffer = sys.stdin.read()
		client_sender(buffer)
	if listen:
		server_loop()

'''

if __name__ == "__main__":
	main()
