import os

print "HI.. Starting the Auto mount & route for the 360 matrix ring"
#Mounting the shared folder
mountcmd = "sudo mount -a"
#print mountcmd
os.system(mountcmd)


#Staring the route for the system
routecmd = "sudo route add -net 224.0.0.0 netmask 240.0.0.0 eth0"
#print routecmd
os.system(routecmd)

os.system("sudo python listener.py")

print "Auto startup DONE"
