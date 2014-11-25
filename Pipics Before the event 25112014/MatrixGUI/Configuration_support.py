#! /usr/bin/env python
#
# Support module generated by PAGE version 4.3.1
# In conjunction with Tcl version 8.6
#    Nov 05, 2014 10:40:43 PM


import sys
from socket import *
import tkMessageBox
import Updating
import time

BCAST_GRP = '192.168.0.255'
BCAST_PORT = 5007

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.bind(('', BCAST_PORT))

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def set_Tk_var():
    # These are Tk variables used passed to Tkinter and must be
    # defined before the widgets using them are created.
    global check
    check = IntVar()

    global spinbox
    spinbox = StringVar()

    global ISO
    ISO = StringVar()

    global Aperature
    Aperature = StringVar()

    global Speed
    Speed = StringVar()

##    global Focus
##    Focus = StringVar()

    global ImageFor
    ImageFor = StringVar()

    global WhiteBalan
    WhiteBalan = StringVar()


def allCams():
    global check
    if check.get():
        w.Spinbox1.configure(state=DISABLED)
        w.Button1.configure(state=DISABLED)
    else:
        w.Spinbox1.configure(state=NORMAL)
        w.Button1.configure(state=NORMAL)


def update():
    global check, spinbox
    updateTime = 4000
    
    if ISO.get() and Aperature.get() and Speed.get() and ImageFor.get() and WhiteBalan.get():
        w.Button2.configure(state=DISABLED)

        outfile="C:\Users\Public\PiPics\ConfigFiles\Set_Configuration.txt"
        writing(outfile)

        if check.get(): #if ALL is selected
            sock.sendto("configure", (BCAST_GRP, BCAST_PORT))
        else:
            if int(spinbox.get())< 10:
                sock.sendto("configure10"+spinbox.get(), (BCAST_GRP, BCAST_PORT))
            else:
                sock.sendto("configure1"+spinbox.get(), (BCAST_GRP, BCAST_PORT))
            

        Updating.create_Updating(root,updateTime)
        root.after(updateTime,enableUpdate)
        #sock.sendto("configure", (BCAST_GRP, BCAST_PORT))

            
    else:
        tkMessageBox.showwarning('Warning', 'Missing data.',parent=root)


def enableUpdate():
    w.Button2.configure(state=NORMAL)
    
    
def writing(outFile):
    global ISO, Aperature, Speed, ImageFor, WhiteBalan
    print("Wriitng on: " + outFile)
    File = open(outFile,'w') # change this directory to the PiPics & file to configure
    File.write(('%s\n%s\n%s\n%s\n%s\n')%(ISO.get(),Aperature.get(),Speed.get(),ImageFor.get(),WhiteBalan.get()))
    File.close()
    return
        

def read():
    if int(spinbox.get()) < 10:
        sock.sendto("getConfigure10"+spinbox.get(), (BCAST_GRP, BCAST_PORT))
    else:
        sock.sendto("getConfigure1"+spinbox.get(), (BCAST_GRP, BCAST_PORT))

    time.sleep(8)
        
    global spinbox, ISO, Aperature, Speed, ImageFor, WhiteBalan
    if int(spinbox.get()) < 61 and int(spinbox.get()) > 0:
        value = ['','','','','']
        
        readfile="C:\Users\Public\PiPics\ConfigFiles\Current_Configuration.txt"
        
        File = open(readfile,'r')
        for i in range(5): #read lines
            line = File.readline()
            line = line.split('\n')
            value[i] = line[0] #store data in list
        ISO.set(value[0])
        Aperature.set(value[1])
        Speed.set(value[2])
        ImageFor.set(value[3])
        WhiteBalan.set(value[4])

def init(top, gui, arg=None):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window ():
    # Function which closes the window_w
    global top_level
    top_level.destroy()
    top_level = None

