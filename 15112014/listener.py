#!/usr/bin/python
import socket
import struct
import fcntl
import subprocess
import sys
import os #Better to use subprocess so that we can get the feedback from the command 
import re
import mpuWithTolera



MCAST_GRP = '224.0.0.0'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

#sock.settimeout(1)

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
	
        global usbStrStart
        
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
                print(resetcmd)
                os.system(resetcmd)
	return
	

def config():
        os.system("sudo python /mnt/PiPics/configureW.py")

def callib():
        os.system("sudo python /home/pi/mpuWithLedTolera.py")

def sensReadnWrite():
        global rpi_id
        count = 100
        values = mpuWithTolera.readSensor()
        CalibrationFile = open('/mnt/PiPics/MatrixGUI/calibration.txt','r+')
        lines = CalibrationFile.readlines()
        CalibrationFile.seek(0)
        for line in lines:
                count += 1
                if count == int(rpi_id):
                        print rpi_id+values[0]+values[1]
                        CalibrationFile.write(('%s.%s.%s\r\n')%(rpi_id,values[0],values[1]))
                        #CalibrationFile.write(('\n')) 
                else:
                        CalibrationFile.readline()

        CalibrationFile.close()


##def checksen():
##    Senprocess = subprocess.Popen(["sudo","/usr/sbin/i2cdetect -y 1"], stdout=subprocess.PIPE , stderr=subprocess.STDOUT )
##    stdout, stderr = Senprocess.communicate()
##
##    sen=stdout.find("68")  #sensor I2c address
##        
##    return sen

doUSBreset()

#imgname = "/mnt/PiPics/" + rpi_id + ".jpg"
imgname = rpi_id + ".jpg"

while True:
        #rcv = 'idle'
        global usbStrStart

##        Senava=checksen()


        #print sock.listen(2)
        
        rcv = sock.recv(10240)
        rcv = rcv.strip()
        print "Command: "+ rcv
        
##        if sock.listen(2)>0:    
##                rcv = sock.recv(10240)
##                rcv = rcv.strip()
##                print "Command: "+ rcv
                
	if rcv == "reboot":
		print "Rebooting..."
		cmd = 'sudo reboot'
		pid = subprocess.call(cmd, shell=True) 
	elif rcv == "resetusb":
                doUSBreset()
        elif rcv == "configure":
                config()
        elif rcv == "calibrate":
##                if Senava == -1:
##                        print " No Sensor "
##                else:
##                        sensReadnWrite() #callib()
                #print rcv
                sensReadnWrite()
        elif rcv == "idle":   #Testing One Calibration File
##                if Senava == -1:
##                        print " No Sensor "
##                else:
##                        sensReadnWrite()
                sensReadnWrite()
                #print rcv
                
        else:
                if usbStrStart == -1:
                        print("No camera Connected")
                else:
                        print "Shooting... "
                        os.system("sudo gphoto2 --auto-detect")
                        capture_cmd = "sudo gphoto2 --capture-image-and-download --filename='" + imgname + "'" + " --force-overwrite"
                        os.system(capture_cmd)
                        os.system("sudo mv " +imgname+ " /mnt/PiPics/"+imgname)
                        print "Image capture done."
                        print "Resetting USB port"
                        doUSBreset()
