
import os
import subprocess

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

Configpath = '/mnt/PiPics/Configuration.txt'
ConfigFile = open( Configpath )

ISO = ConfigFile.readline()
Aperture = ConfigFile.readline()
ShutterSpeed = ConfigFile.readline()
FocusMode = ConfigFile.readline()

ConfigFile.close()

ISO = ISO[0:len(ISO)-2]
Aperture = Aperture[0:len(Aperture)-2]
ShutterSpeed = ShutterSpeed[0:len(ShutterSpeed)-2]
FocusMode = FocusMode[0:len(FocusMode)-2]

print "ISO = " + ISO
print "ISO = "
print ISO + " Done "
print " Done "
print "Aperture = " + Aperture
print "Sutter Speed = " + ShutterSpeed
print "Focus Mode = " + FocusMode


		#Getting rid of the '\n'  at the end of the line since we are reading a line


##----------- Configuring the DSLR with the parameters -----

ISOcmd = "gphoto2 --set-config iso='"+ISO+"' "
print "@----@	Setting ISO to: "+ ISO
#print(ISOcmd)
os.system(ISOcmd)

usbreset()

Aperturecmd = "gphoto2 --set-config aperture='"+Aperture+"' "
print "@----@	Setting Aperture to: "+ Aperture
#print(Aperturecmd)
os.system(Aperturecmd)

usbreset()

ShutterSpeedcmd = "gphoto2 --set-config shutterspeed='"+ShutterSpeed+"' "
print "@----@	Setting ShutterSpeed to: " + ShutterSpeed
#print(ShutterSpeedcmd)
os.system(ShutterSpeedcmd)

usbreset()

FocusModecmd = "gphoto2 --set-config focusmode='"+FocusMode+"' "
print "@----@	Setting FocusMode to: "+ FocusMode
#print(FocusModecmd)
os.system(FocusModecmd)

usbreset()
