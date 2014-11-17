from socket import *
import time
import threading
import struct
# import fcntl
import subprocess
import sys

port = 5007
class PingerThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run (self):
        print 'start thread'
        cs = socket(AF_INET, SOCK_DGRAM)
        cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

        time.sleep(0.1) # issue 3 solved
        cs.sendto('This is a test', ('192.168.0.255', port))
        return

a = PingerThread()
a.start()

#cs = socket(AF_INET, SOCK_DGRAM)
##try:
##    cs.bind(('', port)) # issue 1 solved
##except:
##    print '\nfailed to bind'
##    cs.close()
##    raise
##    cs.blocking(0)

##data = cs.recv(20)  
##print data
##print 'recieved'
##cs.close() # issue 2 solved
