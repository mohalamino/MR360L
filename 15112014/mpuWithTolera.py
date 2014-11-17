#!/usr/bin/python

import smbus
import math
import os
import time
import subprocess

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

def LEDCON( pin , val ):
    ledcmd="echo '"+str(val)+"' > /sys/class/gpio/gpio"+str(pin)+"/value"
    print(ledcmd)
    os.system( ledcmd )

def LEDDIR( pin  ):
    ledcmd="echo 'out' > /sys/class/gpio/gpio"+str(pin)+"/direction"
    print(ledcmd)
    os.system( ledcmd )

def LEDEXP( pin  ):
    ledcmd="echo '"+str(pin) +"'  > /sys/class/gpio/export"
    print(ledcmd)
    os.system( ledcmd )

def WriteOnFile(x,y):
    fil=open("Angles.txt",'w')
    fil.write("X:%d Y%d", x, y)
    fil.close()
    
def checksen():
    Senprocess = subprocess.Popen(["sudo","/usr/sbin/i2cdetect -y 1"], stdout=subprocess.PIPE , stderr=subprocess.STDOUT )
    stdout, stderr = Senprocess.communicate()

    sen=stdout.find("68")  #sensor I2c address
        
    return sen




    
# Now wake the 6050 up as it starts in sleep mode

xRp=0
yRp=0

LEDx=17
LEDy=18

LEDEXP(LEDx)
LEDEXP(LEDy)

LEDDIR(LEDx)
LEDDIR(LEDy)

margin=5

##Senava = checksen()
##
##if Senava == -1:
##    print "No Sensor"
##else:
##    bus.write_byte_data(address, power_mgmt_1, 0)
##



def readSensor():
    
    Senava = checksen()
    #Senava = 1
    
    if Senava == -1:
        print"No Sensor"
    else:
        
        bus.write_byte_data(address, power_mgmt_1, 0)
        global xRp, yRp, LEDx, LEDy
        
        #print "gyro data"
        print "---------=========---------"

        #gyro_xout = read_word_2c(0x43)
        #gyro_yout = read_word_2c(0x45)
        #gyro_zout = read_word_2c(0x47)

        #print "gyro_xout: ", gyro_xout, " scaled: ", (gyro_xout / 131)
        #print "gyro_yout: ", gyro_yout, " scaled: ", (gyro_yout / 131)
        #print "gyro_zout: ", gyro_zout, " scaled: ", (gyro_zout / 131)

        #print
        #print "accelerometer data"
        #print "------------------"

        accel_xout = read_word_2c(0x3b)
        accel_yout = read_word_2c(0x3d)
        accel_zout = read_word_2c(0x3f)

        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0

        #print "accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled
        #print "accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled
        #print "accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled

        #print "x rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
        #print "y rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)

        xR=get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
        yR=get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)

        xR=(xR*(0.5))+(xRp*(0.5))
        yR=(yR*(0.5))+(yRp*(0.5))

        xRp=xR
        yRp=yR
        
        print "X rotation: ", xR
        print "Y rotation: ", yR


        
        if xR >margin or xR<-margin:
            LEDCON(LEDx,1)
            x = 1
        else:
            LEDCON(LEDx,0)
            x = 0

        if yR >margin or yR<-margin:
            LEDCON(LEDy,1)
            y = 1
        else:
            LEDCON(LEDy,0)
            y = 0
        #time.sleep(1)

        values = str(x) + str(y)
        
        return values

