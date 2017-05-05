
#!/bin/python
# Fuck it !!

#imports
import os

#set interface

INTERFACE = 'wlan1mon'
CHANNEL = '6'

# + line[19:37]

def DETECT_MECHANISM(line,type):
	try:
		line.index(type)
		return True
	except ValueError:
		return False

##############################

def FIND_VICTM(type):

	arquivo = open('WPA.HACK') 

	while True: 
		line =  arquivo.readline()
		
		if line == "":
			break
		
		if line.find('#') == -1:
			print 'airodump-ng --channel '  + CHANNEL + ' --bssid ' + line[0:18] +  ' -w file ' + INTERFACE
		
		


	
###########################	
#          MAIN      	  #
###########################	




FIND_VICTM('WPA2') 
