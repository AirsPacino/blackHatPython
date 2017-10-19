# *-* coding:utf-8 *-*

import sys
import getopt
import socket

listen = false
port 
def usage():
	print("usage: " + '\n')
	sys.exit()

def main():
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
			if o in ('h', 'help'):
				usage()
			elif o in ('l', 'listen'):
				








	if not listen and port > 0 and len(target):
		








if __name__ == '__main__':
	main()
