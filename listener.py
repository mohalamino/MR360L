#!/usr/bin/python
import socket
import struct
#import fcntl
import subprocess
import sys
import os #Better to use subprocess so that we can get the feedback from the command 
import re


MCAST_GRP = '224.0.0.0'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


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
