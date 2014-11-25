import subprocess
import os


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

def Getconfig(configuration):
	# Get the config
	Getconfigcmd = "/usr/bin/gphoto2 --get-config "+str(configuration)
	#print Getconfigcmd
	configprocess = subprocess.Popen([Getconfigcmd], stdout=subprocess.PIPE , stderr=subprocess.STDOUT, shell=True )
	stdout, stderr = configprocess.communicate()
	
	#print(stdout)	
	
	Configindexstr = stdout.find("Current: ")
	#print Configindexstr
	Configindexend = stdout.find("Choice")
	#print Configindexend
	ConfigVal = stdout[Configindexstr+9:Configindexend-1]
	print ConfigVal
	

	doUSBreset()
	
	return ConfigVal


iso = Getconfig("iso")
aperture = Getconfig("aperture")
shutterspeed = Getconfig("shutterspeed")
imageformat = Getconfig("imageformat")
whitebalance = Getconfig("whitebalance")


Configpath = '/mnt/PiPics/ConfigFiles/Current_Configuration.txt'
ConfigFile = open( Configpath, 'w' )

ConfigFile.write(('%s\r\n%s\r\n%s\r\n%s\r\n%s\r\n')%(iso, aperture, shutterspeed, imageformat, whitebalance))
ConfigFile.close()
