#!/bin/python3

import sys #allow us to enter command line arguments, among other things
import socket #connect to AF_INET, or sock stream, and to do ip and port connection
from datetime import datetime

#Define our target
#python3 scanner.py <ip>

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate a hostname to IPV4, sys.argv[1] is the <ip>
else:
	print("Invalid amount of arguments")
	print("Syntax: python3 scannner.py <ip>")
	sys.exit()
	
#Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started" + str(datetime.now()))
print("-" * 50)

try:
	for port in range (50,85): #Checking 53 and 80, 53 is for dns.
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1.0) #float, basically it detect the port, and if it's not open, it's going to move on after a second
		result = s.connect_ex((target,port)) #return error indicator: if there's no error, it returns 0
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting Program: KeyboardInterrupted")
	sys.exit
	
except socket.gaierror:
	print("Hostname could not be resoleved")
	sys.exit
	
except socket.error:
	print("Couldn't connect to server")
	sys.exit
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
