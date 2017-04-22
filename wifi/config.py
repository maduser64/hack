
#!/bin/python

# Configura interface para aircrack-ng

import os

print 'escolha rede:'
os.system('airmon-ng')
INTERFACE = raw_input()
active = 'airmon-ng start ' + INTERFACE
os.system(active)
os.system('airmon-ng')
print 'escolha interface'
INTERFACE = raw_input()
active = 'airodump-ng ' + INTERFACE
os.system(active)

	


	
