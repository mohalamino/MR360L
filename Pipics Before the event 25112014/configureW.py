
import os
import subprocess
import re

##-_-_-_-_-_-_-_- IP -_-_-_-_-_-_-_

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

##-_-_-_-_-_-_-_- FUNS -_-_-_-_-_-_-_

def GetDSLRUSB():
	process = subprocess.Popen(['/usr/bin/gphoto2',' ', '--auto-detect'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout, stderr = process.communicate()
	#print(stdout)

	usbStrStart=stdout.find("usb:")
	usbStrEnd=stdout.find(" \nF")

	data = stdout[usbStrStart+4:usbStrEnd]
	dataend = data.find(' ')
	usbportnum = data.find(',')

	usbport = data[usbportnum+1:dataend]
	#print(usbport)
	return usbport


def usbreset():
	usbport=GetDSLRUSB()
	#print(usbport)
	resetcmd = "./usbreset /dev/bus/usb/001/"+usbport
	os.system(resetcmd)

##------------ Reading from Configuration file --------------
#C:\Users\Public\PiPics\ConfigFiles\
#Configpath = '/mnt/PiPics/ConfigFiles/Configuration.txt'

Configpath = '/mnt/PiPics/ConfigFiles/Set_Configuration.txt'
ConfigFile = open( Configpath )

ISO = ConfigFile.readline()
Aperture = ConfigFile.readline()
ShutterSpeed = ConfigFile.readline()
ImageFor = ConfigFile.readline()
WhiteBalan = ConfigFile.readline()

ConfigFile.close()

ISO = ISO[0:len(ISO)-2]
Aperture = Aperture[0:len(Aperture)-2]
ShutterSpeed = ShutterSpeed[0:len(ShutterSpeed)-2]
ImageFor = ImageFor[0:len(ImageFor)-2]
WhiteBalan = WhiteBalan[0:len(WhiteBalan)-2]

#FocusMode = FocusMode[0:len(FocusMode)-2]

print "ISO = " + ISO
print "ISO = "
print ISO + " Done "
print " Done "
print "Aperture = " + Aperture
print "Sutter Speed = " + ShutterSpeed
print "Image Format = " + ImageFor
print "White Balance = " + WhiteBalan

#print "Focus Mode = " + FocusMode


		#Getting rid of the '\n'  at the end of the line since we are reading a line


##----------- Configuring the DSLR with the parameters -----

ISOcmd = "/usr/bin/gphoto2 --set-config iso='"+ISO+"' "
print "@----@	Setting ISO to: "+ ISO
#print(ISOcmd)
os.system(ISOcmd)

usbreset()

Aperturecmd = "/usr/bin/gphoto2 --set-config aperture='"+Aperture+"' "
print "@----@	Setting Aperture to: "+ Aperture
#print(Aperturecmd)
os.system(Aperturecmd)

usbreset()

ShutterSpeedcmd = "/usr/bin/gphoto2 --set-config shutterspeed='"+ShutterSpeed+"' "
print "@----@	Setting ShutterSpeed to: " + ShutterSpeed
#print(ShutterSpeedcmd)
os.system(ShutterSpeedcmd)

usbreset()

ImageForcmd = "/usr/bin/gphoto2 --set-config imageformat='"+ImageFor+"' "
print "@----@	Setting Image Format to: "+ ImageFor
#print(ImageForcmd)
os.system(ImageForcmd)

usbreset()

WhiteBalancmd = "/usr/bin/gphoto2 --set-config whitebalance='"+WhiteBalan+"' "
print "@----@	Setting White Balance to: "+ WhiteBalan
#print(WhiteBalancmd)
os.system(WhiteBalancmd)

usbreset()

##FocusModecmd = "gphoto2 --set-config focusmode='"+FocusMode+"' "
##print "@----@	Setting FocusMode to: "+ FocusMode
###print(FocusModecmd)
##os.system(FocusModecmd)


