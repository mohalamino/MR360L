#!/usr/bin/python
from socket import *
import struct
import fcntl
import subprocess
import sys
import os #Better to use subprocess so that we can get the feedback from the command 
import re


BCAST_GRP = '192.168.0.255'
BCAST_PORT = 5007

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.bind(('', BCAST_PORT))


# DETECT CURRENT IP ADDRESS
ipprocess = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE , stderr=subprocess.STDOUT )
stdout, stderr = ipprocess.communicate()
#print(stdout)

ipstart = stdout.find("inet addr:")
#print(ipstart)
ipend = stdout.find("  Bcast")
#print(ipend)
#print(stdout[ipstart+10:ipend])

ip_address  = re.split('(.*)\.(.*)\.(.*)\.(.*)', stdout[ipstart+10:ipend])

rpi_id = ip_address[4]
print  rpi_id

def doUSBreset():
        # DETECT CURRENT USB

        process = subprocess.Popen(['/usr/bin/gphoto2',' ', '--auto-detect'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = process.communicate()

        usbStrStart=stdout.find("usb:")
        if usbStrStart == -1:
                print("No camera Connected")
        else:
                usbStrEnd=stdout.find(" \nF")

                usbstr = stdout[usbStrStart+4:usbStrEnd]
                usbstrend = usbstr.find(' ')
                usbportnum = usbstr.find(',')

                usbport = usbstr[usbportnum+1:usbstrend]
                print(usbport)
                
                resetcmd = "./usbreset /dev/bus/usb/001/" + usbport
                os.system(resetcmd)
        return
        

def config():
        os.system("sudo python /mnt/PiPics/configureW.py")

def callib():
        os.system("sudo python mpuWithTolera.py")

doUSBreset()

#imgname = "/mnt/PiPics/" + rpi_id + ".jpg"
imgname = rpi_id + ".jpg"

while True:
        rcv = sock.recv(10240)
        rcv = rcv.strip()
        print rcv
        if rcv == "reboot":
                print "Rebooting..."
                cmd = 'sudo reboot'
                pid = subprocess.call(cmd, shell=True) 
        elif rcv == "resetusb":
                doUSBreset()
        elif rcv == "configure":
                config()
        elif rcv == "callibrate":
                callib()
                
        else:
                print "Shooting... " 
                capture_cmd = "sudo gphoto2 --capture-image-and-download --filename='" + imgname + "'" + " --force-overwrite"
                os.system(capture_cmd)
                os.system("sudo mv " +imgname+ " /mnt/PiPics/"+imgname)
                print "Image capture done."
                print "Resetting USB port"
                doUSBreset()
