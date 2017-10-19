# *-* coding:utf-8 *-*

import sys
import getopt
import socket

listen = False
port = 0
target = ''

def usage():
	print("usage: " + '\n')
	sys.exit()

def main():
	global listen
	global port
	global target

	if not len(sys.argv[1:]):
		usage()
	try:
		opt, args = getopts.getopt(sys.argv[1:], "hlp:t:u:e:c",
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
				port = a
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
		client_sender()
		








if __name__ == '__main__':
	main()
